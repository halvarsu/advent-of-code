use std::fs;
use std::time::Instant;

fn main() {
    println!("Hello, world!");
    let file_path = "input";
    let contents = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));
    let start = Instant::now();
    let mut s = 0;
    let lines: Vec<&str> = contents.split("\n").collect();
    let mut num_copies = vec![1; lines.len()-1];
    for (i, line) in lines.iter().enumerate() {
        if line.is_empty(){
            continue
        }
        // println!("{line}");
        let mut winning_numbers: Vec<usize> = Vec::new();
        let mut words = line.split_whitespace();
        words.next();
        words.next();
        let mut number;
        let mut own_numbers = false;
        let mut n: u32 = 0;
        for word in words {
            if word == "|"{
                own_numbers = true;
                continue
            } else {
                number = word.parse::<usize>().expect("Cannot parse as int");
            }
            if own_numbers{
                if winning_numbers.contains(&number){
                    n += 1;
                }
            } else {
                winning_numbers.push(number);
            }
        }
        s += match n {
            exp if exp > 0 => (2 as usize).pow(exp - 1),
            _ => 0,
        };
        for index in i+1..i+1+(n as usize) {
            num_copies[index] += num_copies[i];
        }
    }
    let mut tot_cards = 0;
    for card in num_copies{
        // println!("{card}");
        tot_cards += card;
    }
    println!("s={s}");
    println!("tot cards = {tot_cards}");
    let elapsed = start.elapsed();
    println!("time spent = {:.2?}", elapsed);
}
