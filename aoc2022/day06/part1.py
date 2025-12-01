#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total: int = 4

line: str = my_file_parse[0]

message_good: bool = False

if line[-1] == "\n":
    line = line[:-1]
for i in range(0, len(line)):
    message_good: bool = True
    message :str = line[i:i + 4]
    for letter in message:
        if message.count(letter) != 1:
            message_good = False
    if message_good:
        break
    total += 1

print(total)

# atempt 1 1757 is the result
