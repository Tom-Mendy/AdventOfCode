#!/usr/bin/env python3

total: int = 0
tmp_number: int = 0
all_calories: list[int] = []

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for line in my_file_parse:
    if line == "\n":
        all_calories.append(tmp_number)
        tmp_number = 0
    else:
        tmp_number += int(line)
all_calories.append(tmp_number)

all_calories.sort()
all_calories.reverse()
total = all_calories[0] + all_calories[1] + all_calories[2]
print(total)

# atempt 1 212836 is the result
