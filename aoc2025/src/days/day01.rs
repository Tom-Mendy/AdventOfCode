pub fn run() {
    let input = std::fs::read_to_string("inputs/day01.txt").expect("missing input");

    let result1 = part1(&input);
    println!("Part 1: {}", result1);
    let result2 = part2(&input);
    println!("Part 2: {}", result2);
}

fn part1(input: &str) -> i64 {
    let mut dial = 50;
    let mut time_stop_at_zero: i64 = 0;

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
            time_stop_at_zero += 1;
        }

        dial = normalized;
    }

    time_stop_at_zero
}

fn floor_div(a: i64, b: i64) -> i64 {
    let d = a / b;
    let r = a % b;
    if r != 0 && (r > 0) != (b > 0) {
        d - 1
    } else {
        d
    }
}

fn part2(input: &str) -> i64 {
    let mut dial: i64 = 50;
    let mut time_pass_by_zero: i64 = 0;

    for l in input.lines() {
        let dir = l.chars().next().expect("invalid input");
        let v: i64 = match l[1..].parse() {
            Ok(n) => n,
            Err(_) => panic!("invalid input"),
        };

        match dir {
            'R' => {
                let start = dial;
                let end = start + v;
                // multiples of 100 in (start, end]
                time_pass_by_zero += floor_div(end, 100) - floor_div(start, 100);
                dial = ((end % 100) + 100) % 100;
            }
            'L' => {
                let start = dial;
                let end = start - v;
                // multiples of 100 in [end, start-1] == count of multiples in that range
                time_pass_by_zero += floor_div(start - 1, 100) - floor_div(end - 1, 100);
                dial = ((end % 100) + 100) % 100;
            }
            _ => panic!("invalid input"),
        }
    }

    time_pass_by_zero
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_sample() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n";
        assert_eq!(part1(input), 3);
    }

    #[test]
    fn test_part2_sample() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n";
        assert_eq!(part2(input), 6);
    }

    #[test]
    fn test_part2_sample_step_1() {
        let input = "L68\n";
        assert_eq!(part2(input), 1);
    }

    #[test]
    fn test_part2_sample_step_2() {
        let input = "L68\nL30\n";
        assert_eq!(part2(input), 1);
    }

    #[test]
    fn test_part2_sample_step_3() {
        let input = "L68\nL30\nR48\n";
        assert_eq!(part2(input), 2);
    }

    #[test]
    fn test_part2_sample_step_4() {
        let input = "L68\nL30\nR48\nL5\n";
        assert_eq!(part2(input), 2);
    }

    #[test]
    fn test_part2_sample_step_5() {
        let input = "L68\nL30\nR48\nL5\nR60\n";
        assert_eq!(part2(input), 3);
    }

    #[test]
    fn test_part2_sample_step_6() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\n";
        assert_eq!(part2(input), 4);
    }

    #[test]
    fn test_part2_sample_step_7() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\n";
        assert_eq!(part2(input), 4);
    }

    #[test]
    fn test_part2_sample_step_8() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\n";
        assert_eq!(part2(input), 5);
    }

    #[test]
    fn test_part2_sample_step_9() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\n";
        assert_eq!(part2(input), 5);
    }

    #[test]
    fn test_part2_sample_step_10() {
        let input = "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82\n";
        assert_eq!(part2(input), 6);
    }
}
