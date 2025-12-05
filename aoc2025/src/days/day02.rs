pub fn run() {
    let input = std::fs::read_to_string("inputs/day02.txt").expect("missing input");

    let result1 = part1(&input);
    println!("Part 1: {}", result1);
    let result2 = part2(&input);
    println!("Part 2: {}", result2);
}

fn is_number_palendrom(number: i64) -> bool {
    let s = number.to_string();
    if !s.len().is_multiple_of(2) {
        return false;
    }
    let part1 = &s[..s.len() / 2];
    let part2 = &s[(s.len() / 2)..];
    part1 == part2
}

fn part1(input: &str) -> i64 {
    let mut total = 0;
    let split_by_comma = input.trim().split(',');
    for s in split_by_comma {
        let s = s.trim();
        if s.is_empty() {
            continue;
        }
        let parts: Vec<&str> = s.splitn(2, '-').collect();
        if parts.len() != 2 {
            // skip malformed entry
            eprintln!("warning: skipping malformed range '{}'", s);
            continue;
        }
        let start_number = parts[0].trim().parse::<i64>().unwrap_or(0);
        let end_number = parts[1].trim().parse::<i64>().unwrap_or(start_number);
        for number in start_number..=end_number {
            if is_number_palendrom(number) {
                total += number;
            }
        }
    }
    total
}

fn is_number_patern(number: i64) -> bool {
    let s = number.to_string();
    for index_string in 1..s.len() {
        let sub_string = &s[..index_string];
        let mut is_match = true;
        let len = (s.len() + index_string - 1) / index_string; // ceil division
        for index_sub_string in 0..len {
            let start = index_sub_string * index_string;
            let end = ((index_sub_string + 1) * index_string).min(s.len());
            let part_string = &s[start..end];
            if !part_string.starts_with(sub_string) {
                is_match = false;
                break;
            }
        }
        if is_match {
            return true;
        }
    }
    false
}

fn part2(input: &str) -> i64 {
    let mut total = 0;
    let split_by_comma = input.trim().split(',');
    for s in split_by_comma {
        let s = s.trim();
        if s.is_empty() {
            continue;
        }
        let parts: Vec<&str> = s.splitn(2, '-').collect();
        if parts.len() != 2 {
            // skip malformed entry
            eprintln!("warning: skipping malformed range '{}'", s);
            continue;
        }
        let start_number = parts[0].trim().parse::<i64>().unwrap_or(0);
        let end_number = parts[1].trim().parse::<i64>().unwrap_or(start_number);
        for number in start_number..=end_number {
            if is_number_patern(number) {
                total += number;
            }
        }
    }
    total
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1_sample() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";
        assert_eq!(part1(input), 1227775554);
    }

    #[test]
    fn test_part1_sample_step_1() {
        let input = "11-22";
        assert_eq!(part1(input), 33);
    }

    #[test]
    fn test_part1_sample_step_2() {
        let input = "11-22,95-115";
        assert_eq!(part1(input), 132);
    }

    #[test]
    fn test_part1_sample_step_3() {
        let input = "11-22,95-115,998-1012";
        assert_eq!(part1(input), 1_142);
    }

    #[test]
    fn test_part1_sample_step_4() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890";
        assert_eq!(part1(input), 1_188_513_027);
    }

    #[test]
    fn test_part1_sample_step_5() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224";
        assert_eq!(part1(input), 1_188_735_249);
    }

    #[test]
    fn test_part2_sample() {
        let input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124";
        assert_eq!(part2(input), 4_174_379_265);
    }

    #[test]
    fn test_part2_sample_step_1() {
        let input = "11-22";
        assert_eq!(part2(input), 33);
    }

    #[test]
    fn test_part2_sample_step_2() {
        let input = "11-22,95-115";
        assert_eq!(part2(input), 243);
    }

    #[test]
    fn test_part2_sample_step_3() {
        let input = "11-22,95-115,998-1012";
        assert_eq!(part2(input), 2_252);
    }
}
