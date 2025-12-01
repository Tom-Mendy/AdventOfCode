#!/usr/bin/env python3

total: int = 0
alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for line in my_file_parse:
    if line[-1] == "\n":
        line = line[:-1]
    sections_1: list[str] = line.split(",")[0].split("-")
    sections_1 = [int(i) for i in sections_1]
    sections_2: list[str] = line.split(",")[1].split("-")
    sections_2 = [int(i) for i in sections_2]
    if sections_1[0] >= sections_2[0] and sections_1[1] <= sections_2[1]:
        total += 1
    elif sections_2[0] >= sections_1[0] and sections_2[1] <= sections_1[1]:
        total += 1
    print(sections_1, sections_2)

print(total)

# atempt 1 592 is too high
# atempt 2 556 is the result
