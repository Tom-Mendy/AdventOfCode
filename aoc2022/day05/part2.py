#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

nb_place: int = int(len(my_file_parse[0])/4)

all_places: list[str] = [[] for i in range(nb_place) ]

initilaize: bool = False

for line in my_file_parse:
    if line[-1] == "\n":
        line = line[:-1]
    if not initilaize:
        for i in range(1, len(line), 4):
            if line[i].isalpha():
                all_places[int((i - 1)/4)].append(line[i])
    if initilaize:
        split_line: list[str] = line.split(" ")
        nb_move = int(split_line[1])
        source_place = int(split_line[3]) - 1
        destination_place = int(split_line[5]) - 1
        tmp_place: list[str] = []
        for i in range(nb_move):
            tmp_place.append(all_places[source_place].pop())
        tmp_place.reverse()
        all_places[destination_place].extend(tmp_place)
        
        print(split_line)
    if not initilaize and len(line) == 0:
        for place in all_places:
            place = place.reverse()
        initilaize = True

print(nb_place)
print(all_places)

for place in all_places:
    print(place[-1], end="")

# atempt 1 NLCDCLVMQ is the result
