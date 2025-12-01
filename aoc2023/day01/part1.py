#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


total = 0

nb_int = 0

for line in my_file_parse:
    nb_int = 0
    first_digit = 0
    last_digit = 0
    print(line)
    for j in range(0, len(line), 1):
        letter = line[j]
        if letter.isnumeric():
            print(letter)
            match nb_int:
                case 0:
                    first_digit = int(letter)
                    last_digit = int(letter)
                    nb_int += 1
                case _:
                    last_digit = int(letter)
                    nb_int += 1
    print(first_digit, last_digit)
    tmp_total = first_digit * 10 + last_digit
    print(tmp_total)
    total += tmp_total
    print("#" * 30)


print(total)

# 54081 is the anser
