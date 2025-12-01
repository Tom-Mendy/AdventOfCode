#!/usr/bin/env python3

total: int = 0
alphabet: str = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()


for i in range (0, len(my_file_parse), 3):
    for j in range (0, 3):
        if my_file_parse[i+j][-1] == "\n":
            my_file_parse[i+j] = my_file_parse[i+j][:-1]
    for letter in my_file_parse[i]:
        if letter in my_file_parse[i+1] and letter in my_file_parse[i+2]:
            total += alphabet.index(letter) + 1
            print(letter, alphabet.index(letter) + 1)
            break

print(total)

# atempt 1 2681 is the result
