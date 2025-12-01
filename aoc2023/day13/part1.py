#!/usr/bin/env python3

total = 0

def get_map_in_tab(map: list[str]) -> list[list[str]]:
    empty_line: int = 0
    tmp_map = []
    tab_map = []

    for row in map:
        if row == "":
            tab_map.append(tmp_map)
            tmp_map = []
            empty_line += 1
        else:
            tmp_map.append(row)
    tab_map.append(tmp_map)
    return tab_map

def find_mirror(map: list[list[str]]) -> int:
    len_map = len(map)

    # vertical
    for x in range(1, len(map[0]) - 1):
        mirror = True
        for i in range(0, x):
            len_tkt = x + 1 + i
            if (len_tkt) >= len(map[0]):
                break
            for y in range(0, len_map):
                if map[y][x - i] != map[y][len_tkt]:
                    mirror = False
                    break
        if mirror:
            return x * 100

    # horizontal
    for y in range(1, len_map - 1):
        if map[y] == map[y + 1]:
            mirror = True
            for i in range(0, y):
                len_tkt = y + 1 + i
                if (len_tkt) >= len_map:
                    break
                if map[y - i] != map[len_tkt]:
                    mirror = False
                    break
            if mirror:
                return y + 2

    return 0

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()
for i in range (0, len(my_file_parse)):
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]


tab_map: list[list[str]] = get_map_in_tab(my_file_parse)

for map in tab_map:
    total += find_mirror(map)

print(total)

# attempt 1 26149 is too low

