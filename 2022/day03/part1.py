#!/usr/bin/env python3

total: int = 0
alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for line in my_file_parse:
    if line[-1] == "\n":
        line = line[:-1]
    middle:int = len(line) / 2
    part1: str = line[:int(middle)]
    part2: str = line[int(middle):]
    for letter in part1:
        if letter in part2:
            total += alphabet.index(letter) + 1
            print(letter, alphabet.index(letter) + 1)
            break
    print(part1, part2)

print(total)

# atempt 1 8349 is the result
