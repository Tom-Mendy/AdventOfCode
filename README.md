# AdventOfCode (personal solutions)

This repository contains my Advent of Code solutions across multiple years and languages. Each year is stored in a top-level folder (for example `aoc2022/`, `aoc2023/`, `aoc2024/`, `aoc2025/`) and contains per-day subfolders with inputs and solution files.

## Goals

- **What:** Keep my personal AoC solutions organized and runnable.
- **Languages:** Python (2022, 2023), Go (2024), Rust (2025).
- **Status:** Brief tables below show completion status for each year.

## How the repo is organized

- **`<year>/dayXX/`**: each day has `input.txt`, optional `exemple.txt`, and solution files (`part1.py`, `part2.py`, or `part1.go`, etc.).
- **`aoc2025/`**: a Rust workspace for 2025 solutions (`Cargo.toml`, `src/`).

## Quick Run Instructions

- **Python (2022, 2023):** run a day's part from its folder, for example:

```bash
cd aoc2023/day01
python3 part1.py
python3 part2.py
```

- **Go (2024):** run the `.go` file(s) for a day, for example:

```bash
cd aoc2024/day01
go run part1.go
go run part2.go
```

- **Rust (2025):** build/run the crate in `aoc2025/`:

```bash
cd aoc2025
cargo run --release
```

If the Rust project contains multiple binaries or requires arguments, run via `cargo run -- <args>` or adjust manifest path as needed.

## Contributing / Adding a new day

- Create a new folder `YEAR/dayNN/`.
- Add `input.txt` (your puzzle input) and optional `exemple.txt` (puzzle example input).
- Add solution files following the existing convention: `part1.py` / `part2.py` or `part1.go` / `part2.go`, etc.
- Update the README status table for that year if you want to track progress.

## Status (at a glance)

### 2025

in rust

| day | part 1 | part 2 |
| --- | ------ | ------ |
| 1   | OK     | OK     |
| 2   | OK     | NOT    |

### 2024

in golang

| day | part 1 | part 2 |
| --- | ------ | ------ |
| 1   | OK     | OK     |

### 2023

in python

| day | part 1 | part 2 |
| --- | ------ | ------ |
| 1   | OK     | OK     |
| 2   | OK     | OK     |
| 3   | OK     | OK     |
| 4   | OK     | OK     |
| 5   | OK     | OK     |
| 6   | OK     | OK     |
| 7   | OK     | OK     |
| 8   | OK     | NO     |
| 9   | OK     | OK     |
| 10  | OK     | NO     |
| 11  | OK     | NO     |
| 12  | OK     | NO     |
| 13  | NO     | NO     |

### 2022

in python

| day | part 1 | part 2 |
| --- | ------ | ------ |
| 1   | OK     | OK     |
| 2   | OK     | OK     |
| 3   | OK     | OK     |
| 4   | OK     | OK     |
| 5   | OK     | OK     |
| 6   | OK     | OK     |
| 7   | SKIP   | SKIP   |
| 8   | OK     | OK     |

## Notes & Tips

- Use `python3` for Python solutions. Consider a virtualenv if you add dependencies.
- `go run` executes Go solution files directly — ensure you have Go installed.
- For Rust, use the stable toolchain appropriate to your code; `rustup` can manage toolchains.

If you want, I can also:

- add a small top-level script to run a specific day's solutions across languages,
- or add CI to run all solutions for a given year automatically.
