use std::fs;

fn read_input(file_path: &str) -> String {
    let contents =
        fs::read_to_string(file_path).expect(&format!("No input file found at {file_path}"));
    return contents;
}

fn read_line_part1(line: &str) -> Vec<usize> {
    return line
        .split_whitespace()
        .filter_map(|i| i.parse::<usize>().ok())
        .collect()
}

fn read_line_part2(line: &str) -> usize {
    let mut split = line.split(":");
    split.next();
    return split
        .next()
        .expect("oops1")
        .replace(" ", "")
        .parse::<usize>()
        .expect("oops2");
}

fn calc_winning_interval(time: usize, distance: usize) -> usize {
    let t = time as f64;
    let r = distance as f64;
    let sqrt_num = (t*t - 4.0*r).sqrt();
    let lower_lim = (t - sqrt_num) / 2.0;
    let upper_lim = (t + sqrt_num) / 2.0;
    println!("up: {upper_lim} low:{lower_lim}");

    let delta = 0.0 == (upper_lim - (upper_lim as usize as f64));
    return (upper_lim.ceil() - lower_lim.ceil()) as usize - delta as usize;
}

fn run(file_path: &str, part: usize) {
    let contents = read_input(file_path);

    let mut lines = contents.split("\n");
    let times;
    let distances;
    if part == 1 {
        times = read_line_part1(lines.next().expect("could not read line"));
        distances = read_line_part1(lines.next().expect("could not read line"));
    } else if part == 2{
        times = vec![read_line_part2(lines.next().expect("could not read line"))];
        distances = vec![read_line_part2(lines.next().expect("could not read line"))];
    } else {
        panic!();
    }
    println!("{times:?}");
    println!("{distances:?}");

    let mut margin: usize = 1;
    for (t, d) in times.into_iter().zip(distances){
        let wins = calc_winning_interval(t, d);
        println!("t {t}, d {d}, wins {wins}");
        margin *= wins;
    }
    println!("margin: {margin}", );

}

fn main() {
    run("input", 1);
    run("input", 2);

}
