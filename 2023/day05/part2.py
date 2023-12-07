#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

index_tab_map = -1

tab_maps = [[]  for i in range (0, 7)]

seeds = my_file_parse[0][:-1].split(":")[1][1:].split(" ")

seeds = [int(seed) for seed in seeds]

print("seeds =", seeds)

for i in range(1, len(my_file_parse)):
    if ":" in my_file_parse[i]:
        index_tab_map += 1
    else:
        if my_file_parse[i][0].isnumeric():
            if my_file_parse[i][-1] == "\n":
                line = my_file_parse[i][:-1].split(" ")
            else :
                line = my_file_parse[i].split(" ")
            for k in range (len(line)):
                line[k] = int(line[k])
            tab_maps[index_tab_map].append(line)

search_seed = True

i = 0

while search_seed:
    i += 1
    tmp_total = i
    for j in range (len(tab_maps) - 1, -1, -1):
        tab_maps[j]
        for line in tab_maps[j]:
            if tmp_total >= line[0] and tmp_total < line[0] + line[2]:
                tmp_total = line[1] + (tmp_total - line[0])
                break
    for j in range (0, len(seeds), 2):
        if tmp_total >= seeds[j] and tmp_total < seeds[j] + seeds[j + 1]:
            search_seed = False
            break
    print("i =", i, "tmp_total =", tmp_total)

print("Total = ", i)

# attempt 1 102900316 is too hight
# attempt 2 79004094 is the result so long

