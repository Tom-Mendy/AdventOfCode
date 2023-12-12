#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 0

def diferance_two_number(list_of_values: list[int], index: int) -> int:
    if index == 0:
        return 0
    else:
        return list_of_values[index] - list_of_values[index - 1]
    
def prediction_of_the_next_value(list_of_values: list[int]) -> int:
    next = 0
    all_tab = []
    all_tab.append(list_of_values)
    for i in range(0, len(list_of_values) - 1):
        all_tab.append([])
    for i in range(1, len(list_of_values)):
        for j in range(1, len(all_tab[i - 1])):
            all_tab[i].append(diferance_two_number(all_tab[i - 1], j))
    print(all_tab)
    for i in range(len(all_tab) - 1, -1, -1):
        next = (all_tab[i][0] - next)
    return next


for i in range (0, len(my_file_parse)):
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]
    my_file_parse[i] = my_file_parse[i].split(" ")
    my_file_parse[i] = list(map(int, my_file_parse[i]))

for line in my_file_parse:
    print(line)
    tmp = prediction_of_the_next_value(line)
    print(tmp)
    total += tmp
print(total)

# attempt 1 923 the result

