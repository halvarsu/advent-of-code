use std::fs;
use std::collections::HashMap;
// use reduce::Reduce;

use ::phf::{Map, phf_map};
// struct Round {
//     count: String,
//     colour: String,
// }

const MAX_CUBES : Map<&'static str, u32> = phf_map!{
    "red" => 12,
    "green" => 13,
    "blue" => 14,
};

fn main() {
    println!("Hello, world!");

    let file_path = "../input";
    let contents = fs::read_to_string(file_path)
        .expect(&format!("No input file found at {file_path}"));

    let mut total_id = 0;
    let mut total_power = 0;


    for line in contents.split("\n") {
        if line.is_empty() {
            continue
        }
        let mut split = line.split(":");
        let game = split.next().unwrap();
        let rounds = split.next().expect("Empty game!").split(";");

        let mut valid = true;


        let mut min_cubes = HashMap::new();

        min_cubes.insert("red", 0);
        min_cubes.insert("green", 0);
        min_cubes.insert("blue", 0);
        

        println!("------------------------ {} ------------------------", game);
        for (i, round) in rounds.enumerate(){
            println!("round={}: {}", i, round);
            for cubes in round.split(",") {
                let cube_info = cubes.split_whitespace().collect::<Vec<&str>>();
                let [count_string, colour] = cube_info.as_slice() else { panic!() };

                let count = count_string.parse::<u32>().unwrap();
                // println!("count={} colour={}", count_string, colour);
                if count > MAX_CUBES[colour] {
                    valid = false;
                }
                
                if count > min_cubes[colour] {
                    min_cubes.insert(colour, count);
                }
            }
        }
        let game_id = game.split_whitespace().last().unwrap().parse::<u32>().unwrap();
        // let c = min_cubes.clone();
        // println!("{} {} {}", 
        //     c.get("red").unwrap(),
        //     c.get("green").unwrap(),
        //     c.get("blue").unwrap());
        let power: u32 = min_cubes.into_values().reduce(|a, b| a*b).unwrap();
        total_power += power;


        println!("game_id={}, valid={}, power={}", game_id, valid, power);
        if valid {
            total_id += game_id;
        }
    }
    println!("----------------------------------------------------------");
    println!("total id={}, total power={}", total_id, total_power)


}



