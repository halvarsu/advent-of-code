use std::fs;
use regex::Regex;
use ::phf::{Map, phf_map};

fn main() {
    let re = Regex::new(r"\d").unwrap();

    run_regex(re, false);

    run_part2();

}


fn run_regex(re: Regex, verbose: bool) {
    let file_path = "../input";
    let contents = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));


    let mut first_digit: regex::Match;
    let mut last_digit: regex::Match;
    let mut matches: regex::Matches;
    let mut s = 0;
    for line in contents.split("\n"){
        if verbose{
            // print!("line:{line},");
        }
        if line.is_empty() {
            if verbose{
                println!("skipping empty line");
            }
            continue
        }
        matches = re.find_iter(line);
        first_digit = matches.next().expect("No matches");
        last_digit = matches.last().unwrap_or(first_digit);
        if verbose {  
            println!("{} {}", first_digit.as_str(), last_digit.as_str());
}
        s += 10 * parse_digit(first_digit.as_str()) + parse_digit(last_digit.as_str());
    }
    println!("s={}", s)
}

// fn reverse(string: &str) -> String{
//     return string.chars().rev().collect::<String>();
// }


fn run_part2() {
    let patterns: &str = r"0|1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero";

    let file_path = "../input";
    let contents: String = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));

    let mut s = 0;
    // let mut i = 0;
    for line in contents.split("\n"){
        // print!("{} ", line);
        let mut first_digit_index = line.len()+1;
        let mut last_digit_index: isize = -1;
        let mut first_digit = "0";
        let mut last_digit = "0";
        for pat in patterns.split('|'){
            let new_min_ind = line.find(pat).unwrap_or(first_digit_index);
            if new_min_ind < first_digit_index {
                first_digit_index = new_min_ind;
                first_digit = pat;
            }

            let new_max_ind = line.rfind(pat);
            if new_max_ind.is_none() {

            } else if new_max_ind.unwrap() as isize > last_digit_index {
                last_digit_index = new_max_ind.unwrap() as isize;
                last_digit = pat;
            }
            // if i == 987 {
            //     println!("{} {} {} {}", pat, new_max_ind.unwrap_or(100), last_digit_index, last_digit)
            // }
        }
        s += 10 * parse_digit(first_digit) + parse_digit(last_digit);
        println!("{} {} {} {} {}", first_digit_index, last_digit_index, first_digit, last_digit, line);
        // i+=1;
        // println!("{} {}", first_digit, last_digit);
        // let new_max_ind = line.rfind(pat).unwrap_or(last_digit_index);

    }
    println!("s={}", s);
}

fn parse_digit(string_digit: &str) -> u32{
    let string_to_num : Map<&'static str, u32> = phf_map!{
        "one" => 1,
        "two" => 2,
        "three" => 3,
        "four" => 4,
        "five" => 5,
        "six" => 6,
        "seven" => 7,
        "eight" => 8,
        "nine" => 9,
        "zero" => 0,
    };

    let result = string_digit.parse::<u32>();
    return match result {
        Ok(int) => return int,
        Err(_) => string_to_num[string_digit],
    };
}
