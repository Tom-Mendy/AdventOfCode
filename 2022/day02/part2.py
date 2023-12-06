#!/usr/bin/env python3

your_total_score: int = 0
your_round_score: int = 0

enemies_moves: list[str] = ["A", "B", "C"]
your_moves: list[str] = ["X", "Y", "Z"]

file = open("./exemple.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for line in my_file_parse:
    your_round_score = 0
    if line[-1] == "\n":
        line = line[:-1]
    line = line.split(" ")
    enemies_move = enemies_moves.index(line[0])
    # draw
    if line[1] == "Y":
        your_round_score += enemies_move + 1
        your_round_score += 3
    else:
        # win
        if line[1] == "Z":        
            my_move = enemies_move + 1
            if my_move > 2:
                my_move = 0
            your_round_score += my_move + 1
            your_round_score += 6
        # loose
        else:
            my_move = enemies_move - 1
            if my_move < 0:
                my_move = 2
            your_round_score += my_move + 1
            your_round_score += 0
    print("your round score: ", your_round_score)
    your_total_score += your_round_score

print(your_total_score)

# atempt 1 13448 is the result
