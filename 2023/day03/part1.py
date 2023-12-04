#!/usr/bin/env python3


def is_adjacent_symbol_function(x: int, y: int, map: list[str]) -> bool:
    # top
    if y - 1 >= 0:
        if map[y - 1][x] != "." and not map[y - 1][x].isnumeric():
            return True
        if x - 1 >= 0:
            if map[y - 1][x - 1] != "." and not map[y - 1][x - 1].isnumeric():
                return True
        if x + 1 < len(map[y]):
            if map[y - 1][x + 1] != "." and not map[y - 1][x + 1].isnumeric():
                return True
    # middle
    if x - 1 >= 0:
        if map[y][x - 1] != "." and not map[y][x - 1].isnumeric():
            return True
    if x + 1 < len(map[y]):
        if map[y][x + 1] != "." and not map[y][x + 1].isnumeric():
            return True
    # bottom
    if y + 1 < len(map):
        if map[y + 1][x] != "." and not map[y + 1][x].isnumeric():
            return True
        if x - 1 >= 0:
            if map[y + 1][x - 1] != "." and not map[y + 1][x - 1].isnumeric():
                return True
        if x + 1 < len(map[y]):
            if map[y + 1][x + 1] != "." and not map[y + 1][x + 1].isnumeric():
                return True
    return False


total: int = 0
tmp_number: int = 0
is_adjacent_symbol: bool = False

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for i in range(0, len(my_file_parse)):
    tmp_number = 0
    is_adjacent_symbol = False
    for j in range(0, len(my_file_parse[i])):
        letter: chr = my_file_parse[i][j]
        if letter.isnumeric():
            tmp_number = tmp_number * 10 + int(letter)
            if not is_adjacent_symbol:
                is_adjacent_symbol = is_adjacent_symbol_function(j, i, my_file_parse)
        else:
            if is_adjacent_symbol:
                total += tmp_number
            tmp_number = 0
            is_adjacent_symbol = False
    if is_adjacent_symbol:
        total += tmp_number

print(total)

# atempt 1 519044 too hight
# atempt 2 7775 too low
# atempt 3 20607 too low
