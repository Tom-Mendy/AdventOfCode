#!/usr/bin/env python3

file = open("./input.txt", 'r');
my_file_parse: list[str] = file.readlines()
file.close()

total = 0

for line in my_file_parse:
    tmp_total = 0
    line = line[:-1]
    winnig_number = line.split("|")[0].split(":")[1].split(" ")
    winnig_number = [item for item in winnig_number if item != '']
    numbers = line.split("|")[1].split(" ")
    numbers = [item for item in numbers if item != '']
    print(winnig_number)
    print(numbers)
    for nb in winnig_number:
        if nb in numbers:
            tmp_total += 1
    if tmp_total > 0:
        tmp_total = 2 ** (tmp_total - 1)
        print(tmp_total)
        total += tmp_total

print(total)

# attempt 1 823 too low
# attempt 2 21959 the result