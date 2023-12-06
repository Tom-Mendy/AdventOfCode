#!/usr/bin/env python3

def is_good_character_function(y: int, x: int,map: list[str]) -> bool:
    special_characters: str = "#*$%&@!/=+^?-_~:;<>{}[]()|\\"
    return map[y][x] in special_characters
    

def is_adjacent_symbol_function(x: int, y: int, map: list[str]) -> bool:
    # top
    if y - 1 >= 0:
        if is_good_character_function(y - 1, x, map):
            return True
        if x - 1 >= 0:
            if is_good_character_function(y - 1, x - 1, map):
                return True
        if x + 1 < len(map[y]):
            if is_good_character_function(y - 1, x + 1, map):
                return True
    # middle
    if x - 1 >= 0:
        if is_good_character_function(y, x - 1, map):
            return True
    if x + 1 < len(map[y]):
        if is_good_character_function(y, x + 1, map):
            return True
    # bottom
    if y + 1 < len(map):
        if is_good_character_function(y + 1, x, map):
            return True
        if x - 1 >= 0:
            if is_good_character_function(y + 1, x - 1, map):
                return True
        if x + 1 < len(map[y]):
            if is_good_character_function(y + 1, x + 1, map):
                return True
    return False


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
        if letter.isnumeric():
            tmp_number = tmp_number * 10 + int(letter)
            if not is_adjacent_symbol:
                is_adjacent_symbol = is_adjacent_symbol_function(x, y, my_file_parse)
        else:
            if is_adjacent_symbol:
                total += tmp_number
            tmp_number = 0
            is_adjacent_symbol = False

print(total)

# atempt 1 519044 too hight
# atempt 2 7775 too low
# atempt 3 20607 too low
# atempt 4 517021 is the result
