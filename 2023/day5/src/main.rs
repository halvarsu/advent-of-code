use std::fs;
// use std::collections::HashMap;
use std::num::ParseIntError;

use itertools::Itertools;
use std::ops::Range;

mod ranges {
    use std::ops::Range;
    pub struct RangeMap {
        pub keys: Range<usize>,
        pub vals: Range<usize>,
        // pub length: usize,
        // Prevents initializing via fields, which could lead to invalid mappings
        validator: (),
    }

    impl RangeMap {
        pub fn new(key_start: usize, val_start: usize, length: usize) -> RangeMap {
            return RangeMap {
                keys: (key_start..key_start + length),
                vals: (val_start..val_start + length),
                // length,
                validator: (),
            };
        }
        pub fn map_val(&self, val:usize, ) -> usize{
            // TODO: add error handling on underflow
            // assert!(self.keys.contains(&val));
            return (val - self.keys.start) + self.vals.start;
        }

        pub fn map_range(&self, range: Range<usize>) -> Range<usize> {
            return self.map_val(range.start)..self.map_val(range.end);
        }
    }

}

use ranges::RangeMap;

fn trivial_parse_sources(line: &str) -> Vec<Range<usize>> {
    // Parses each entry as a range (i..i+1) for use in part 1.
    return line
        .split_whitespace()
        .filter_map(|i| i.parse::<usize>().ok())
        .map(|i| i..i+1)
        .collect();
}

fn parse_sources(line: &str) -> Vec<Range<usize>> {
    // Parses each pair of entries (a, b) into a range (a..a+b) for use in part 2.
    return line
        .split_whitespace()
        .filter_map(|i| i.parse::<usize>().ok())
        .tuples()
        .map(|(start, length)| (start..(start + length)))
        .collect();
}

pub fn run(file_path: &str, iterations: usize, part: usize) -> Vec<Range<usize>> {
    let contents = read_input(file_path);

    let mut lines = contents.split("\n");
    let mut sources: Vec<Range<usize>>;
    if part == 1 {
        sources = trivial_parse_sources(lines.next().unwrap());
    } else {
        sources = parse_sources(lines.next().unwrap());
    }
    let mut i = 0;
    let mut maps: Vec<RangeMap> = Vec::new();

    for line in lines {
        if line.contains("map") {
            i += 1;
            if i > iterations {
                break;
            }
        } else if let Some([val_start, key_start, map_length]) = parse_line(line) {
            let range_map = RangeMap::new(key_start, val_start, map_length);
            maps.push(range_map);
        } else if line.is_empty() {
            if !maps.is_empty() {
                sources = map_sources(sources, &maps);
                // println!("sources = {sources:?}");
                // println!("maps = [", );
                // for map in maps.iter() {
                    // println!("    {:?} -> {:?}", map.keys, map.vals);
                // }
                // println!("{line}");
                maps = Vec::new();
            }
            continue;
        } else {
            println!("Weird line: {line}");
        }
    }
    return sources;
}

fn split_and_map_source(source: Range<usize>, map: &RangeMap) -> [Vec<Range<usize>>; 2] {
    let new_sources: Vec<Range<usize>>;
    let mapped: Vec<Range<usize>>;

    let source_start_in_map: bool = map.keys.contains(&source.start);
    let source_end_in_map: bool = map.keys.contains(&source.end);
    if source_start_in_map & source_end_in_map {
        // source is entirely inside map
        mapped = vec![map.map_range(source)];
        new_sources = vec![];
    } else if source_start_in_map {
        // source starts but does not end in map
        mapped = vec![map.map_val(source.start)..map.vals.end];
        new_sources = vec![map.keys.end..source.end];
    } else if source_end_in_map {
        // source ends but does not start in map
        mapped = vec![map.vals.start..map.map_val(source.end)];
        new_sources = vec![source.start..map.keys.start];
    } else {
        if (source.start < map.keys.start) & (source.end >= map.keys.end) {
            // source starts before and ends after map
            mapped = vec![map.vals.start..map.vals.end];
            new_sources = vec![source.start..map.keys.start,
                               map.keys.end..source.end];
        } else {
            // there is no overlap between source and map
            mapped = vec![];
            new_sources = vec![source];
        }
    }
    return [new_sources, mapped];
}


fn map_sources(sources: Vec<Range<usize>>, maps: &Vec<RangeMap>) -> Vec<Range<usize>> {
    let split_sources = sources
        .iter()
        .fold(vec![], |acc, source|
            acc
            .into_iter()
            .chain(
                map_source(source.clone(), maps)
                .into_iter())
            .collect());
    return split_sources;
}


fn map_source(source: Range<usize>, maps: &Vec<RangeMap>) -> Vec<Range<usize>> {
    let mut unmapped: Vec<Range<usize>> = vec![source];
    let mut mapped: Vec<Range<usize>> = vec![];

    for map in maps {
        let mut split_sources: Vec<Range<usize>> = vec![];
        for tmp_source in unmapped {
            let [mut _split_sources, mut _mapped] = split_and_map_source(tmp_source, &map);
            split_sources.append(&mut _split_sources);
            mapped.append(&mut _mapped);
        }
        unmapped = split_sources
            .into_iter()
            .filter(|source| !source.is_empty())
            .collect();
    }
    mapped.append(&mut unmapped);

    return mapped;
}

fn read_input(file_path: &str) -> String {
    let contents =
        fs::read_to_string(file_path).expect(&format!("No input file found at {file_path}"));
    return contents;
}

fn parse_line(line: &str) -> Option<[usize; 3]> {
    let split: Vec<Result<usize, ParseIntError>> = line
        .split_whitespace()
        .map(|i| i.parse::<usize>())
        .collect();
    if split.len() == 0 {
        return None;
    }
    let mut result: Vec<usize> = Vec::new();

    for val in split {
        result.push(match val {
            Ok(value) => value,
            Err(_) => return None,
        });
    }
    return Some(
        result
            .try_into()
            .unwrap_or_else(|v: Vec<usize>| panic!("Expected 3 numbers, got {}", v.len())),
    );
}

fn find_min(output: Vec<Range<usize>>) -> usize{
    return output
        .iter()
        .filter(|range| !range.is_empty())
        .map(|range| range.start)
        .min()
        .expect("Oops!");
}

fn main() {
    let part1 = find_min(run("input", 100, 1));
    println!("part1:{:?}", part1);

    let part2 = find_min(run("input", 100, 2));
    println!("part2:{:?}", part2);

    // let min = out.iter().min().expect("Oops!");

    // let out2 = run("input", 100, 2);
    // let min2 = out2.iter().min().expect("Oops!");
    // println!("part2:{min2:?}");
}

#[cfg(test)]
mod tests{
    use super::*;

    // Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
    // Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
    // Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
    // Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

    #[test]
    fn soil() {
        let result = find_min(run("test_input", 1, 1));
        assert_eq!(result, 13);
    }

    #[test]
    fn fert() {
        let result = find_min(run("test_input", 2, 1));
        assert_eq!(result, 52);
    }

    #[test]
    fn water() {
        let result = find_min(run("test_input", 3, 1));
        assert_eq!(result, 41);
    }

    #[test]
    fn all_iter() {
        let result = find_min(run("test_input", 100, 1));
        assert_eq!(result, 35);
    }

    #[test]
    fn test_part2() {
        let result = find_min(run("test_input", 100, 2));
        assert_eq!(result, 46);
    }
}
