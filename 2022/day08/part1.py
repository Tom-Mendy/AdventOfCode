#!/usr/bin/env python3


def is_visible(x: int, y:int, map: list[str]) -> bool:
    result: bool = True
    for mouving_x in range (x + 1, len(map[y])):
        if map[y][x] <= map[y][mouving_x]:
            result = False
            break
    if result:
        return result
    result = True
    for mouving_x in range (0, x):
        if map[y][x] <= map[y][mouving_x]:
            result = False
            break
    if result:
        return result
    result = True
    for mouving_y in range (y + 1, len(map)):
        if map[y][x] <= map[mouving_y][x]:
            result = False
            break
    if result:
        return result
    result = True
    for mouving_y in range (0, y):
        if map[y][x] <= map[mouving_y][x]:
            result = False
            break
    return result


file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

my_file_parse = [line[:-1] for line in my_file_parse]

for y in range (0, len(my_file_parse)):
    print(my_file_parse[y])

total: int = 0

total = (len(my_file_parse) - 1) * 4

visibles: bool = False

for y in range (1, len(my_file_parse) - 1):
    for x in range (1, len(my_file_parse) - 1):
        if is_visible(x, y, my_file_parse):
            total += 1
print(total)

# atempt 1 1870 is the result
