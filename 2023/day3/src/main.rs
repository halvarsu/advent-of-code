use std::fs;
use regex::Regex;
use std::collections::HashMap;

fn pad_with_dots(contents: String) -> String {
    let lines: Vec<&str> = contents.split("\n").collect();
    let line_length = lines[0].len();
    let dot_line = String::from_utf8(vec![b'.'; line_length+2]).expect("Heisann!");

    let new_content = contents.replace("\n", ".\n.");
    let new_new_content = format!("{}\n.{}{}", dot_line, new_content, dot_line);
    return new_new_content;
}

fn main() {
    // println!("Hello, world!");

    let file_path = "input";
    let unpadded_contents = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));
    let contents = pad_with_dots(unpadded_contents);
    let mut printable = contents.clone() as String;
    let schematic = contents.clone(); // .replace("\n", "") as String;

    let lines: Vec<&str> = contents.split("\n").collect();
    let line_length = lines[0].len() + 1;
    let row_count = lines
        .iter()
        .filter(|x| !x.is_empty())
        .count();
    // println!("line length {line_length}");
    // println!("row count {row_count}");

    for line in &lines{
        // println!("{}", line);
    }
    let mut gears: HashMap<usize, (usize, usize)> = HashMap::new();

    let re = Regex::new(r"[\d]+").unwrap();
    let mut sum = 0;

    // for result in re.find_iter(&contents.replace("\n", "")){
    for result in re.find_iter(&contents){
        let result_str = result.as_str();
        let result_val = result_str.parse::<usize>().expect("Could not parse result as integer");

        let neighbors = get_surrounding(result, &schematic, line_length);
        let neighbors_locs = get_neighbor_locs(result, line_length);

        let neighbor_string: String = neighbors.join("");
        let neighbor_loc_vec = neighbors_locs.into_iter().flatten().collect::<Vec<usize>>();

        // print!("locs: ");
    
        for i in 0..neighbor_string.len(){
            let symb = neighbor_string.as_bytes()[i] as char;
            let loc = neighbor_loc_vec[i];
            // print!("{}={}, ", symb, loc);
        }
        // println!("");

        for (index, _) in neighbor_string.match_indices('*'){
            let gear_loc = neighbor_loc_vec[index];
            // insert 1 or increment if not existing
            gears.entry(gear_loc)
                .and_modify(|(a, b)| {
                    *a+=1;
                    *b*=result_val}
                )
                .or_insert((1, result_val));
            // println!("gear {gear_loc}")
        }

        // // println!("lengths {} {}", neighbor_string.len(), neighbors_locs.into_iter().flatten().count());

        // println!("{}", neighbor_string);

        let no_symb_reg = Regex::new(r"[^.\d]").unwrap();
        let neighbor_symbol = no_symb_reg.find(&neighbor_string);

        if let Some(value) = neighbor_symbol {
            sum += result_val;
            let range = result.start()..result.end();
            let replace_string = String::from_utf8(vec![b'X'; result.as_str().len()]).unwrap();
            // let replace_string = format!(r"\x1b[31;42m{result_str}abc\x1b[0m");
            // printable.replace_range(range, &replace_string);
            // println!("Value! {} {replace_string}", value.as_str());
        } else {
            // println!("No value");
        }
    }

    let mut total_power = 0;
    for (gear_loc, (connecting_parts, power)) in gears.iter() {
        // printable.replace_range(*gear_loc..*gear_loc+1, &connecting_parts.to_string());
        if *connecting_parts == 2 {
            total_power += power;
            // let gear_loc_corr
            // // printable.replace_range(*gear_loc..*gear_loc+1, "o")
            // // printable.replace_range(*gear_loc..*gear_loc+1, &connecting_parts.to_string());
        } else {
            // // printable.replace_range(*gear_loc..*gear_loc+1, "i")
        }
        // println!("connecting_parts {connecting_parts} power {power}");
    }
    // // printable = printable.replace("o", "█");
    // // printable = printable.replace("i", "▒");
    // println!("{printable}");
    // println!("sum {sum}");
    // println!("power {total_power}");
}

fn get_neighbor_locs(result: regex::Match, line_length: usize) -> [Vec<usize>; 4]{
    let start: usize = result.start();
    let end: usize = result.end();
    // println!("in gnl {line_length} {start} {end}");
    return [
        vec![start - 1],
        vec![end],
        (start-line_length-1..end-line_length+1).collect(),
        (start+line_length-1..end+line_length+1).collect()
    ]
}

fn get_surrounding(result: regex::Match, schematic: &str, line_length: usize) -> [String; 4] {
    let start = result.start();
    let end = result.end();

    let row: usize = start / line_length;
    let col_start: usize = start % line_length;
    let col_end: usize = end % line_length;

    // println!("{line_length} {row} {col_start} {col_end}");
    let before: char = schematic.as_bytes()[start - 1] as char;
    let after: char = schematic.as_bytes()[end] as char;

    let above: String = schematic.get(start - 1 - line_length..end + 1 - line_length).expect("OOPS!").to_string();
    let below: String = schematic.get(start - 1 + line_length..end + 1 + line_length).expect("OOPS!").to_string();

    // print!("1 ");
    // println!("{}", above);
    // print!("2 ");
    // print!("{}", before);
    // print!("{}", result.as_str());
    // print!("{}", after);
    // println!("");
    // print!("3 ");
    if col_start == 0{
        // print!("x");
    }

    // println!("{}", below);
    // print!("4 ");
    if col_end == line_length {
        // print!("x");
    }
    // println!("");

    return [before.to_string(),after.to_string(),above,below];
}
