#!/usr/bin/env python3

def expend_universe(universe: list[str]) -> list[str]:
    expension_mutilplier: int = 1000000
    #expend the universe verticaly
    empty: bool = True
    x = 0
    while x < len(universe[0]):
        empty = True
        for y in range(0, len(universe)):
            if universe[y][x] == "#":
                empty = False
                break
        if empty:
            print("Vertical Expend")
            for i in range(0, expension_mutilplier - 1):
                for y in range(0, len(universe)):
                    universe[y].insert(x, ".")
                x += 1
        x += 1
    #expend the universe horizontaly
    empty: bool = True
    y = 0
    len_universe = len(universe[0])
    new_line = ["." for i in range(0, len_universe)]
    while y < len(universe):
        empty = True
        for x in range(0, len_universe):
            if universe[y][x] == "#":
                empty = False
                break
        if empty:
            print("Horizontal Expend")
            for i in range(0, expension_mutilplier - 1):
                universe = universe[:y] + [new_line] + universe[y:]
                y += 1
        y += 1
    print("Expend done")
    return universe

def name_galaxies(universe: list[str]) -> list[list[str]]:
    name: chr = '1'
    len_y: int = len(universe)
    len_x: int = len(universe[0])
    galaxy_book: list[list[str]] = []
    for y in range(0, len_y):
        if '#' in universe[y]:
            for x in range(0, len_x):
                if universe[y][x] == '#':
                    universe[y][x] = name
                    galaxy_book.append((x, y))
                    name = chr(ord(name) + 1)
    return galaxy_book

def generate_pairs(galaxy_book: list[list[str]]) -> list[list[str]]:
    pairs: list[list[str]] = []
    for i in range (0, len(galaxy_book)):
        for j in range (i + 1, len(galaxy_book)):
            pairs.append([i + 1, j + 1])
    return pairs

def calculate_distance(galaxy_book: list[list[str]], pairs: list[list[str]]) -> int:
    total = 0
    for pair in pairs:
        distance: int = 0
        for i in range(0, 2):
            distance += abs(galaxy_book[pair[0] - 1][i] - galaxy_book[pair[1] - 1][i])
        total += distance
    return total

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()
for i in range (0, len(my_file_parse)):
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]
    my_file_parse[i] = list(my_file_parse[i])

total = 0

# for line in my_file_parse:
#     for i in line:
#         print(i, end="")
#     print()

# print()

my_file_parse = expend_universe(my_file_parse)
print("start naming galaxies")
galaxy_book = name_galaxies(my_file_parse)
print("end naming galaxies")
print("start generating pairs")
pairs = generate_pairs(galaxy_book)
print("end generating pairs")
print("start calculating distance")
total = calculate_distance(galaxy_book, pairs)
print("end calculating distance")

print(galaxy_book)
print(pairs, len(pairs))

# for line in my_file_parse:
#     for i in line:
#         print(i, end="")
#     print()

print(total)

# attempt 1 10422930 the result

