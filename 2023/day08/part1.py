#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 0

path_tab_KEY = []
path_tab_VALUE = []

movement = my_file_parse[0][:-1]

for i in range(2, len(my_file_parse)):
    tmp_tab = []
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]
    my_file_parse[i] = my_file_parse[i].split(" ")
    tmp_tab.append(my_file_parse[i][2][1:-1])
    tmp_tab.append(my_file_parse[i][3][:-1])
    path_tab_KEY.append(my_file_parse[i][0])
    path_tab_VALUE.append(tmp_tab)

print(movement)
print(path_tab_KEY)
print(path_tab_VALUE)

find = False

curent_position = "AAA"

while not find:
    for move in movement:
        match move:
            case "R":
                curent_position = path_tab_VALUE[path_tab_KEY.index(curent_position)][1]
            case "L":
                curent_position = path_tab_VALUE[path_tab_KEY.index(curent_position)][0]
        total += 1
        if curent_position == "ZZZ":
            find = True

print(total)

# attempt 1 12643 the result

