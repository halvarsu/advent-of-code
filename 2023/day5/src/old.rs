pub fn part1(file_path: &str, iterations: usize) -> Vec<usize> {
    let contents = read_input(file_path);

    let mut seed2location: BiMap<usize,usize> = BiMap::new();
    let mut lines = contents.split("\n");
    let first_line = lines.next();
    // Get all integers on first line:
    let seeds: Vec<usize> = first_line
        .unwrap()
        .split_whitespace()
        .filter_map(|i| i.parse::<usize>().ok())
        .collect();
    
    let mut i = 0;
    let mut prev_map = seed2location.clone();
    for line in lines{
        println!("i={i}");
        
        let parsed_values = parse_line(line);
        if let Some([dest_start, source_start, range_length]) = parsed_values {
            // println!("Parse successful, {dest_start} {source_start} {range_length}");
            seed2location = map_source2dest(
                &prev_map, seed2location, dest_start, source_start, range_length);

        }

        if line.contains("map") {
            prev_map = seed2location.clone();
            i += 1;
            // map_index += 1;
            for source in 1..100 {
                if let Some(dest) = seed2location.get_by_left(&source) {
                    // println!("a={source} b={:?}", dest);
                } else {
                    // println!("a={source} b={source} !");
                }
            }
            if i > iterations {
                
                break;
            }

            for seed in seeds.clone() {
                // print!("seed={seed} ");
                // println!("out={:?}", seed2location.get_by_left(&seed).unwrap_or(&seed));
            }
        }
    }
    // for seed in seeds.clone() {
    //     print!("seed={seed} ");
    //     println!("loc={:?}", seed2location.get_by_left(&seed).unwrap_or(&seed));
    // }

    let locations: Vec<usize> = seeds.iter().map(|seed| *seed2location.get_by_left(&seed).unwrap_or(&seed)).collect();
    return locations;


}



fn map_source2dest(old_map: &BiMap<usize,usize>, mut new_map: BiMap<usize,usize>, dest_start: usize, source_start: usize, range_length: usize) -> BiMap<usize, usize> {
    for i in 0..range_length {
        let source = source_start + i;
        let dest = dest_start + i;
        let key = *old_map.get_by_right(&source).unwrap_or(&source);
        // println!("source={source}, dest={dest}. Mapping key={key} to dest={dest} default={}", key==source);
        new_map.insert(key, dest);
        // map.insert(source_start + i, 
        //     *map.get_by_right(&(dest_start + i))
        //         .unwrap_or(&(dest_start+i)));
    }
    return new_map;
}

