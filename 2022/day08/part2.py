#!/usr/bin/env python3


def is_visible(x: int, y:int, map: list[str]) -> int:
    right: int = 0
    for mouving_x in range (x + 1, len(map[y])):
        right += 1
        if map[y][x] <= map[y][mouving_x]:
            break
    left: int = 0
    for mouving_x in range (x - 1, -1, -1):
        left += 1
        if map[y][x] <= map[y][mouving_x]:
            break
    bottom: int = 0
    for mouving_y in range (y + 1, len(map)):
        bottom += 1
        if map[y][x] <= map[mouving_y][x]:
            break
    top: int = 0
    for mouving_y in range (y - 1, -1, -1):
        top += 1
        if map[y][x] <= map[mouving_y][x]:
            break
    return right * left * bottom * top


file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

my_file_parse = [line[:-1] for line in my_file_parse]

for y in range (0, len(my_file_parse)):
    print(my_file_parse[y])

total: int = 0

for y in range (1, len(my_file_parse) - 1):
    for x in range (1, len(my_file_parse) - 1):
        tmp_total = is_visible(x, y, my_file_parse)
        if tmp_total > total:
            total = tmp_total
print(total)

# atempt 1 517440 is the result
