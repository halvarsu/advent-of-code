use itertools::Itertools;
use std::collections::HashMap;
use std::fs;

fn read_input(file_path: &str) -> String {
    let contents =
        fs::read_to_string(file_path).expect(&format!("No input file found at {file_path}"));
    return contents;
}

fn read_hand(line: &str, part: usize) -> Hand {
    let mut split = line.split_whitespace();
    let hand_str = split.next().unwrap();
    let bid = split.next().unwrap().parse::<usize>().expect("oops!");
    return Hand::new(hand_str, bid, part);
}

fn get_hand_val(cards: [char; 5], part: usize) -> usize {
    let mut hand_val: usize = 0;
    for card in cards {
        hand_val *= 13;
        hand_val += evaluate_card(card, part);
    }
    return hand_val;
}

fn evaluate_card(card: char, part: usize) -> usize {
    if part == 1 {
        return "23456789TJQKA"
            .find(card)
            .expect(&format!("Could not find card {card}"));
    } else if part == 2 {
        return "J23456789TQKA"
            .find(card)
            .expect(&format!("Could not find card {card}"));
    } else {
        panic!("");
    }
}

#[derive(Eq, PartialEq, Ord, PartialOrd, Copy, Clone, Debug)]
enum Label {
    HighCard,
    OnePair,
    TwoPair,
    ThreeOfAKind,
    FullHouse,
    FourOfAKind,
    FiveOfAKind,
}

#[derive(Eq, PartialEq, Ord, PartialOrd, Debug)]
struct Hand {
    label: Label,
    hand_val: usize,
    cards: [char; 5],
    bid: usize,
}

impl Hand {
    fn new(hand_str: &str, bid: usize, part: usize) -> Hand {
        let cards: [char; 5] = hand_str.chars().collect::<Vec<char>>().try_into().unwrap();
        let hand_val = get_hand_val(cards, part);
        let mut label = label_hand(hand_str);
        if part == 2 {
            let old_label = label;
            let num_jokers = cards.iter().filter(|c| **c == 'J').count();
            label = make_stronger(&old_label, num_jokers);
            if old_label != label {
                // println!("{hand_str:?}: {old_label:?} -> {label:?}, {num_jokers}");
            }
        }
        return Hand {
            label,
            hand_val,
            cards,
            bid,
        };
    }
}

fn count_cards(hand_str: &str) -> HashMap<char, usize> {
    let mut card_counts: HashMap<char, usize> = HashMap::new();
    for card in hand_str.chars() {
        *card_counts.entry(card).or_insert(0) += 1;
    }
    return card_counts;
}

fn make_stronger(label: &Label, num_jokers: usize) -> Label {
    match (label, num_jokers) {
        (_, 0) => *label,
        (Label::HighCard, 1) => return Label::OnePair,
        (Label::OnePair, 1 | 2) => return Label::ThreeOfAKind,
        (Label::TwoPair, 1) => return Label::FullHouse,
        (Label::TwoPair, 2) => return Label::FourOfAKind,
        (Label::ThreeOfAKind, 1 | 3) => return Label::FourOfAKind,
        (Label::FullHouse, 2 | 3) => return Label::FiveOfAKind,
        (Label::FourOfAKind, 1 | 4) => return Label::FiveOfAKind,
        (Label::FiveOfAKind, 5) => return Label::FiveOfAKind,
        (_, _) => panic!("Invalid label-joker combination {:?} {}", label, num_jokers),
    }
}

fn label_hand(hand_str: &str) -> Label {
    let card_counts = count_cards(&hand_str);
    let unique = card_counts.len();
    let three_equal = card_counts.values().contains(&3);

    return match (unique, three_equal) {
        (5, _) => Label::HighCard,
        (4, _) => Label::OnePair,
        (3, true) => Label::ThreeOfAKind,
        (3, false) => Label::TwoPair,
        (2, true) => Label::FullHouse,
        (2, false) => Label::FourOfAKind,
        (1, _) => Label::FiveOfAKind,
        _ => panic!("Invalid hand {}", hand_str),
    };
}

fn run(file_path: &str, part: usize) {
    let contents = read_input(file_path);
    println!("{file_path} | part={part}");

    let lines = contents.split("\n");
    let mut hands: Vec<Hand> = lines
        .filter(|line| !line.is_empty())
        .map(|line| read_hand(line, part))
        .collect();
    hands.sort();

    let mut total_score: usize = 0;
    for (i, hand) in hands.iter().enumerate() {
        let rank = i + 1;
        let score = rank * hand.bid;
        total_score += score;
        // println!("{:4}*{:4} ={:7} {:?}, {:?}", hand.bid, rank, score, hand.label, hand.cards);
    }
    println!("Total score: {total_score}");
    println!("");
}

fn main() {
    run("test_input", 1);
    run("test_input", 2);
    run("input", 1);
    run("input", 2);
}
