pub fn run() {
    let input = std::fs::read_to_string("inputs/day01.txt")
        .expect("missing input");

    let result1 = part1(&input);
    println!("Part 1: {}", result1);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_sample() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n";
        assert_eq!(part1(input), 3);
    }
}

fn part1(input: &str) -> i64 {
    let mut dial = 50;
    let mut time_pass_by_zero: i64 = 0;

    for l in input.lines() {
        let dir = l.chars().next().expect("invalid input");
        let v: i64 = match l[1..].parse() {
            Ok(n) => n,
            Err(_) => panic!("invalid input"),
        };

        let new_rotation = match dir {
            'L' => dial - v,
            'R' => dial + v,
            _ => panic!("invalid input"),
        };

        // normalize into 0..99 range
        let mut normalized = new_rotation % 100;
        if normalized < 0 {
            normalized += 100;
        }

        if normalized == 0 {
            time_pass_by_zero += 1;
        }

        dial = normalized;
    }

    time_pass_by_zero
}
