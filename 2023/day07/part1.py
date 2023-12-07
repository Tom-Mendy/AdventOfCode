#!/usr/bin/env python3

file = open("./exemple.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 0

all_lines = []

for line in my_file_parse:
    line_split = line.split(" ")
    line_split[1] = int(line_split[1])
    # determine type of hand
    tab_letter = []
    tab_nb_letter = []
    for letter in line_split[0]:
        if letter not in tab_letter:
            tab_letter.append(letter)
            tab_nb_letter.append(0)
        tab_nb_letter[tab_letter.index(letter)] += 1
    print(tab_letter, tab_nb_letter)
    if 5 in tab_nb_letter:
        line_split.append(7)
    elif 4 in tab_nb_letter:
        line_split.append(6)
    elif 3 in tab_nb_letter and 2 in tab_nb_letter:
        line_split.append(5)
    elif 3 in tab_nb_letter:
        line_split.append(4)
    elif 2 in tab_nb_letter:
        if tab_nb_letter.count(2) == 2:
            line_split.append(3)
        else:
            line_split.append(2)
    else:
        line_split.append(1)
    all_lines.append(line_split)
    print(line_split)

cards = "AKQJT98765432" 

# sort by type of hand
all_lines.sort(key=lambda x: x[2])
for j in range(len(all_lines)):
    for i in range(len(all_lines) - 1):
        line_1 = all_lines[i]
        line_2 = all_lines[i + 1]
        if line_1[2] == line_2[2]:
            for k in range(len(line_1[0])):
                strenght_card_1 = cards.index(line_1[0][k])
                strenght_card_2 = cards.index(line_2[0][k])
                if strenght_card_1 > strenght_card_2:
                    break
                if strenght_card_1 < strenght_card_2:
                    all_lines[i], all_lines[i + 1] = all_lines[i + 1], all_lines[i]
                    break

print(all_lines)

for i in range(len(all_lines)):
    total += all_lines[i][1] * (i + 1)

print(total)

# attempt 1 248923598 too hight
# attempt 2 247842715 too hight
# attempt 3 247815719 the result

