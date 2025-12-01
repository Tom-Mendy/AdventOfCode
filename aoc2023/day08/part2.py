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

curents_position = []

for key in path_tab_KEY:
    if key[2] == "A":
        curents_position.append(key)

print(curents_position)

len_curent_position = len(curents_position)

while not find:
    for move in movement:
        if not find:
            for i in range (0, len_curent_position):
                match move:
                    case "R":
                        curents_position[i] = path_tab_VALUE[path_tab_KEY.index(curents_position[i])][1]
                    case "L":
                        curents_position[i] = path_tab_VALUE[path_tab_KEY.index(curents_position[i])][0]
            total += 1
            nb_z = 0
            for curent_position in curents_position:
                if curent_position[2] != "Z":
                    break
                nb_z += 1
            print(curents_position, nb_z, total)
            if nb_z == len_curent_position:
                find = True

print(total)

# attempt 1 12643 the result