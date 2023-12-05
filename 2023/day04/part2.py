#!/usr/bin/env python3

file = open("./input.txt", 'r');
my_file_parse: list[str] = file.readlines()
file.close()

total = 0

tab = [1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1]

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
    for i in range (1, tmp_total + 1):
        tab[i] += 1 * tab[0]
    print(tab[0])
    total += tab[0]
    for i in range (0, len(tab) - 1):
        tab[i] = tab[i + 1]
    tab[-1] = 1

print(total)

# attempt 1 5132675 the result