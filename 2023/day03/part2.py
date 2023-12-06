#!/usr/bin/env python3

def get_number(y: int, x: int,map: list[str]) -> int:
    number: int = 0
    start_x: int = x
    for i in range(x, -1, -1):
        if map[y][i].isnumeric():
            start_x = i
        else:
            break
    for i in range(start_x, len(map[y])):
        if map[y][i].isnumeric():
            number = number * 10 + int(map[y][i])
        else:
            break
    return number

def is_good_character_function(y: int, x: int,map: list[str]) -> bool:
    return map[y][x].isnumeric()

def is_adjacent_symbol_function(x: int, y: int, map: list[str]) -> list[int]:
    total: list[int] = []
    # top
    if y - 1 >= 0:
        if is_good_character_function(y - 1, x, map):
            total.append(get_number(y - 1, x, map))
        if x - 1 >= 0:
            if is_good_character_function(y - 1, x - 1, map):
                total.append(get_number(y - 1, x - 1, map))
        if x + 1 < len(map[y]):
            if is_good_character_function(y - 1, x + 1, map):
                total.append(get_number(y - 1, x + 1, map))
    # middle
    if x - 1 >= 0:
        if is_good_character_function(y, x - 1, map):
            total.append(get_number(y, x - 1, map))
    if x + 1 < len(map[y]):
        if is_good_character_function(y, x + 1, map):
            total.append(get_number(y, x + 1, map))
    # bottom
    if y + 1 < len(map):
        if is_good_character_function(y + 1, x, map):
            total.append(get_number(y + 1, x, map))
        if x - 1 >= 0:
            if is_good_character_function(y + 1, x - 1, map):
                total.append(get_number(y + 1, x - 1, map))
        if x + 1 < len(map[y]):
            if is_good_character_function(y + 1, x + 1, map):
                total.append(get_number(y + 1, x + 1, map))
    total.sort()
    temp = total[0]
    total = [total[x] for x in range (1, len(total)) if total[x] != total[x - 1]]
    total.append(temp)
    return total


total: int = 0
tmp_number: int = 0
is_adjacent_symbol: bool = False

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for y in range(0, len(my_file_parse)):
    tmp_number = 0
    is_adjacent_symbol = False
    for x in range(0, len(my_file_parse[y])):
        letter: chr = my_file_parse[y][x]
        if letter == "*":
            nb_number = is_adjacent_symbol_function(x, y, my_file_parse)
            if len(nb_number) == 2:
                total += nb_number[0] * nb_number[1]


print(total)

# atempt 1 81296995 is the result
