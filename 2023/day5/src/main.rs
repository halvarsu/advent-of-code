use std::fs;
// use std::collections::HashMap;
use std::num::ParseIntError;


pub fn run(file_path: &str, iterations: usize, part: u32) -> Vec<usize> {
    let contents = read_input(file_path);

    let mut lines = contents.split("\n");
    let first_line = lines.next();
    // Get all integers on first line:
    let mut sources: Vec<usize> = first_line
        .unwrap()
        .split_whitespace()
        .filter_map(|i| i.parse::<usize>().ok())
        .collect();

    // sources = range_pairs_to_sources(sources);
    
    let mut i = 0;
    // let mut dests: Vec<usize> = Vec::new();
    println!("length of sources: {}", sources.len());

    let mut parsing = True;

    let mut dest_starts: Vec<usize> = Vec::new();
    let mut source_starts: Vec<usize> = Vec::new();
    let mut range_lengths: Vec<usize> = Vec::new();

    for line in lines{
        if let Some([dest_start, source_start, range_length]) = parse_line(line) {
            dest_starts.push(dest_start);
            source_starts.push(source_start);
            range_lengths.push(range_length);
        } else if line.contains("map") {
            sources = split_and_map_sources(&sources, dest_starts, source_starts, range_lengths);

            dest_starts = Vec::new();
            source_starts = Vec::new();
            range_lengths = Vec::new();

            i += 1;
            if i > iterations {
                break;
            }
        } else if line.is_empty() {
            continue;
        } else {
            println!("Weird line: {line}");
        }
    }
    return sources;
}

fn split_and_map_sources(sources: &Vec<usize>, dest_starts: Vec<usize>, source_starts: Vec<usize>, range_lengths: Vec<usize>) -> Vec<usize> {
    let dests: Vec<usize> = Vec::new();
    for i in 1..source_starts.len() {
        for source_pair in sources.chunks(2) {
        }
    }
    source_starts;
    // for source_pair in sources.chunks(2) {


    //     for (i, source_start) in source_starts.iter().enumerate() {
    //         if in_range(*source_start, source_pair[0], source_pair[1]){
    //             let source_end = *source_start + range_lengths[i];
    //         }
    //     }
    // }
        // a source pair can:
        // be outside all ranges
        // start before the range and go into it but not past
        // start before the range and go past it
        // start in the range but not go past it
        // start in the range and go past it
        //
        // a range can: 
        // not touch a source pair
        // split a source pair
    return dests;
}


fn source_range2dest_range(sources: &Vec<usize>, mut dests: Vec<usize>, dest_start: usize, source_start: usize, range_length: usize) -> Vec<usize> {
    for (i, source) in sources.iter().enumerate() {
        if in_range(*source, source_start, range_length) {

            let offset = source - source_start;
            let dest = dest_start + offset;
            dests[i] = dest;
            // println!("source={source} dest={dest}, ds={dest_start}, ss={source_start}, rl={range_length}");
        }
    }
    return dests;
}


fn source2dest(sources: &Vec<usize>, mut dests: Vec<usize>, dest_start: usize, source_start: usize, range_length: usize) -> Vec<usize> {
    for (i, source) in sources.iter().enumerate() {
        if in_range(*source, source_start, range_length) {

            let offset = source - source_start;
            let dest = dest_start + offset;
            dests[i] = dest;
            // println!("source={source} dest={dest}, ds={dest_start}, ss={source_start}, rl={range_length}");
        }
    }
    return dests;
}

fn in_range(val: usize, start: usize, length: usize) -> bool {
    // returns offset if in range, else None
    return (start <= val) & (val < start + length)
}


fn read_input(file_path: &str) -> String {
    let contents = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));
    return contents;
}


fn parse_line(line: &str) -> Option<[usize; 3]>{
    let split: Vec<Result<usize, ParseIntError>> = line.split_whitespace().map(|i| i.parse::<usize>()).collect();
    if split.len() == 0 {
        return None;
    }
    let mut result: Vec<usize> = Vec::new();

    for val in split {
        result.push(match val {
            Ok(value) => value,
            Err(_) => return None
        });
    }
    return Some(result.try_into().unwrap_or_else(|v: Vec<usize>| panic!("Expected 3 numbers, got {}", v.len())));
}




fn main() {
    let out = run("input", 100, 1);
    let min = out.iter().min().expect("Oops!");
    println!("part1:{min:?}");

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
    fn test_range_pairs_to_sources() {
        let input = vec![4, 3, 10, 5];
        let result = vec![4, 5, 6, 10, 11, 12, 13, 14];
        assert_eq!(result, range_pairs_to_sources(input));
    }

    #[test]
    fn soil() {
        let result = run("/home/halvard/projects/advent-of-code/2023/day5/test_input", 1, 1);
        assert_eq!(result, vec![81, 14, 57, 13]);
    }

    #[test]
    fn fert() {
        let result = run("/home/halvard/projects/advent-of-code/2023/day5/test_input", 2, 1);
        assert_eq!(result, vec![81, 53, 57, 52]);
    }

    #[test]
    fn water() {
        let result = run("/home/halvard/projects/advent-of-code/2023/day5/test_input", 3, 1);
        assert_eq!(result, vec![81, 49, 53, 41]);
    }


    #[test]
    fn all_iter() {
        let result = run("/home/halvard/projects/advent-of-code/2023/day5/test_input", 100, 1);
        assert_eq!(result, vec![82, 43, 86, 35]);
    }

    #[test]
    fn test_part2() {
        let result = run("/home/halvard/projects/advent-of-code/2023/day5/test_input", 100, 2);
        let min = result.iter().min().expect("Oops!");
        assert_eq!(min, &46);
    }
}
