mod days;

fn main() {
    let day = std::env::args()
        .nth(1)
        .expect("use: cargo run -- <day>");

    match day.as_str() {
        "1" => days::day01::run(),
        _ => println!("Day {day} not implemented"),
    }
}