pub fn run() {
    let input = std::fs::read_to_string("inputs/day03.txt").expect("missing input");

    let result1 = part1(&input);
    println!("Part 1: {}", result1);
    let result2 = part2(&input);
    println!("Part 2: {}", result2);
}

fn part1(input: &str) -> i64 {
    let mut total = 0;
    let split_by_line = input.lines();
    for bank in split_by_line {
        let mut largest_possible_joltage = 0;
        let left_digit_list = &bank[..bank.len() - 1];
        for (index, left_digit) in left_digit_list.chars().enumerate() {
            let right_digit_list = &bank[index + 1..];
            for right_digit in right_digit_list.chars() {
                let mut digits = String::new();
                digits.push(left_digit);
                digits.push(right_digit);
                let actual_number = match digits.parse() {
                    Ok(number) => number,
                    _ => panic!(),
                };
                if actual_number > largest_possible_joltage {
                    largest_possible_joltage = actual_number;
                }
            }
        }
        total += largest_possible_joltage;
    }
    total
}

fn part2(input: &str) -> i64 {
    0
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_sample() {
        let input = "987654321111111
811111111111119
234234234234278
818181911112111";
        assert_eq!(part1(input), 357);
    }

    #[test]
    fn test_part1_sample_step_1() {
        let input = "987654321111111";
        assert_eq!(part1(input), 98);
    }

    #[test]
    fn test_part1_sample_step_2() {
        let input = "987654321111111
811111111111119";
        assert_eq!(part1(input), 187);
    }
}
