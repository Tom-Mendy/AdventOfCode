#!/usr/bin/env python3

def find_start(my_file_parse: list[str]) -> [int, int]:
    for y in range(0, len(my_file_parse)):
        for x in range(0, len(my_file_parse[0])):
            if my_file_parse[y][x] == "S":
                return [x, y]

def move_after(my_file_parse: list[str], map_nb_move: list[str], curent_position: list[int], nb_move: int) -> None:
    move_state = True
    while move_state:
        move_state = False
        map_nb_move[curent_position[1]][curent_position[0]] = nb_move
        # North
        if my_file_parse[curent_position[1]][curent_position[0]] == "|" or my_file_parse[curent_position[1]][curent_position[0]] == "L" or my_file_parse[curent_position[1]][curent_position[0]] == "J" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
            if my_file_parse[curent_position[1] - 1][curent_position[0]] == "|" or my_file_parse[curent_position[1] - 1][curent_position[0]] == "7" or my_file_parse[curent_position[1] - 1][curent_position[0]] == "F":
                if map_nb_move[curent_position[1] - 1][curent_position[0]] == "." or map_nb_move[curent_position[1] - 1][curent_position[0]] > nb_move + 1:
                    curent_position = [curent_position[0], curent_position[1] - 1]
                    nb_move += 1
                    move_state = True
                    
        # South
        if not move_state:
            if my_file_parse[curent_position[1]][curent_position[0]] == "|" or my_file_parse[curent_position[1]][curent_position[0]] == "7" or my_file_parse[curent_position[1]][curent_position[0]] == "F" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
                if my_file_parse[curent_position[1] + 1][curent_position[0]] == "|" or my_file_parse[curent_position[1] + 1][curent_position[0]] == "L" or my_file_parse[curent_position[1] + 1][curent_position[0]] == "J":
                    if map_nb_move[curent_position[1] + 1][curent_position[0]] == "." or map_nb_move[curent_position[1] + 1][curent_position[0]] > nb_move + 1:
                        curent_position = [curent_position[0], curent_position[1] + 1]
                        nb_move += 1
                        move_state = True
            # East
            if not move_state:
                if my_file_parse[curent_position[1]][curent_position[0]] == "-" or my_file_parse[curent_position[1]][curent_position[0]] == "F" or my_file_parse[curent_position[1]][curent_position[0]] == "L" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
                    if my_file_parse[curent_position[1]][curent_position[0] + 1] == "-" or my_file_parse[curent_position[1]][curent_position[0] + 1] == "J" or my_file_parse[curent_position[1]][curent_position[0] + 1] == "7":
                        if map_nb_move[curent_position[1]][curent_position[0] + 1] == "." or map_nb_move[curent_position[1]][curent_position[0] + 1] > nb_move + 1:
                            curent_position = [curent_position[0] + 1, curent_position[1]]
                            nb_move += 1
                            move_state = True
                # West
                if not move_state:
                    if my_file_parse[curent_position[1]][curent_position[0]] == "-" or my_file_parse[curent_position[1]][curent_position[0]] == "J" or my_file_parse[curent_position[1]][curent_position[0]] == "7" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
                        if my_file_parse[curent_position[1]][curent_position[0] - 1] == "-" or my_file_parse[curent_position[1]][curent_position[0] - 1] == "F" or my_file_parse[curent_position[1]][curent_position[0] - 1] == "L":
                            if map_nb_move[curent_position[1]][curent_position[0] - 1] == "." or map_nb_move[curent_position[1]][curent_position[0] - 1] > nb_move + 1:
                                curent_position = [curent_position[0] - 1, curent_position[1]]
                                nb_move += 1
                                move_state = True
    return None

def move(my_file_parse: list[str], map_nb_move: list[str], curent_position: list[int], nb_move: int) -> None:
    map_nb_move[curent_position[1]][curent_position[0]] = nb_move
    # North
    if my_file_parse[curent_position[1]][curent_position[0]] == "|" or my_file_parse[curent_position[1]][curent_position[0]] == "L" or my_file_parse[curent_position[1]][curent_position[0]] == "J" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
        if my_file_parse[curent_position[1] - 1][curent_position[0]] == "|" or my_file_parse[curent_position[1] - 1][curent_position[0]] == "7" or my_file_parse[curent_position[1] - 1][curent_position[0]] == "F":
            if map_nb_move[curent_position[1] - 1][curent_position[0]] == "." or map_nb_move[curent_position[1] - 1][curent_position[0]] > nb_move + 1:
                move_after(my_file_parse, map_nb_move, [curent_position[0], curent_position[1] - 1], nb_move + 1)
    # South
    if my_file_parse[curent_position[1]][curent_position[0]] == "|" or my_file_parse[curent_position[1]][curent_position[0]] == "7" or my_file_parse[curent_position[1]][curent_position[0]] == "F" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
        if my_file_parse[curent_position[1] + 1][curent_position[0]] == "|" or my_file_parse[curent_position[1] + 1][curent_position[0]] == "L" or my_file_parse[curent_position[1] + 1][curent_position[0]] == "J":
            if map_nb_move[curent_position[1] + 1][curent_position[0]] == "." or map_nb_move[curent_position[1] + 1][curent_position[0]] > nb_move + 1:
                move_after(my_file_parse, map_nb_move, [curent_position[0], curent_position[1] + 1], nb_move + 1)
    # East
    if my_file_parse[curent_position[1]][curent_position[0]] == "-" or my_file_parse[curent_position[1]][curent_position[0]] == "F" or my_file_parse[curent_position[1]][curent_position[0]] == "L" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
        if my_file_parse[curent_position[1]][curent_position[0] + 1] == "-" or my_file_parse[curent_position[1]][curent_position[0] + 1] == "J" or my_file_parse[curent_position[1]][curent_position[0] + 1] == "7":
            if map_nb_move[curent_position[1]][curent_position[0] + 1] == "." or map_nb_move[curent_position[1]][curent_position[0] + 1] > nb_move + 1:
                move_after(my_file_parse, map_nb_move, [curent_position[0] + 1, curent_position[1]], nb_move + 1)
    # West
    if my_file_parse[curent_position[1]][curent_position[0]] == "-" or my_file_parse[curent_position[1]][curent_position[0]] == "J" or my_file_parse[curent_position[1]][curent_position[0]] == "7" or my_file_parse[curent_position[1]][curent_position[0]] == "S":
        if my_file_parse[curent_position[1]][curent_position[0] - 1] == "-" or my_file_parse[curent_position[1]][curent_position[0] - 1] == "F" or my_file_parse[curent_position[1]][curent_position[0] - 1] == "L":
            if map_nb_move[curent_position[1]][curent_position[0] - 1] == "." or map_nb_move[curent_position[1]][curent_position[0] - 1] > nb_move + 1:
                move_after(my_file_parse, map_nb_move, [curent_position[0] - 1, curent_position[1]], nb_move + 1)
    return None


file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 0




for i in range (0, len(my_file_parse)):
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]

map_nb_move = [["." for x in my_file_parse[0]] for y in my_file_parse]

start = find_start(my_file_parse)

print(start)

for line in my_file_parse:
    print(line)
for line in map_nb_move:
    print(line)

move(my_file_parse, map_nb_move, start, 0)

for line in map_nb_move:
    for nb in line:
        if nb != "." and nb > total:
            total = nb

for line in my_file_parse:
    print(line)
for line in map_nb_move:
    line = [str(x) for x in line]
    print(line)

print(total)

# attempt 1 6875 the result

