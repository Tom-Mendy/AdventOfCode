#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 0
cards = "AKQT98765432J"

all_lines = []

def witch_hand(tab_nb_letter: list[int]) -> int:
    if 5 in tab_nb_letter:
        return 7
    elif 4 in tab_nb_letter:
        return 6
    elif 3 in tab_nb_letter and 2 in tab_nb_letter:
        return 5
    elif 3 in tab_nb_letter:
        return 4
    elif 2 in tab_nb_letter:
        if tab_nb_letter.count(2) == 2:
            return 3
        else:
            return 2
    else:
        return 1

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
    # attribute strenght of hand
    if "J" in tab_letter:
        max_var = 0
        for card in cards:
            if card != "J":
                tmp_line_split = line_split[0].replace("J", card)
                tmp_tab_letter = []
                tmp_tab_nb_letter = []
                for letter in tmp_line_split:
                    if letter not in tmp_tab_letter:
                        tmp_tab_letter.append(letter)
                        tmp_tab_nb_letter.append(0)
                    tmp_tab_nb_letter[tmp_tab_letter.index(letter)] += 1
                tmp_max = witch_hand(tmp_tab_nb_letter)
                if tmp_max > max_var:
                    max_var = tmp_max
        line_split.append(max_var)
            
    else:
        line_split.append(witch_hand(tab_nb_letter))
    all_lines.append(line_split)
    print(line_split)
    print(tab_letter, tab_nb_letter)


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

# attempt 1 249351022 too hight
# attempt 2 248681902 too low
# attempt 3 248747492 is the result
