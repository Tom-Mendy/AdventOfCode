#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

# 12 red cubes, 13 green cubes, and 14 blue cubes.

total = 0

for line in my_file_parse:
    print("#" * 30)
    print(line)
    number_game = int(line.split(":")[0].split(" ")[1])
    print(number_game)
    bag_of_color = line.split(":")[1][:-1]
    # get all the colors
    sub_pouch = bag_of_color.split(";")

    work = True
    for tmp in sub_pouch:
        red = 0
        blue = 0
        green = 0
        nb_colors = tmp.split(",")
        for nb_color in nb_colors:
            nb_color = nb_color[1:].split(" ")
            print(nb_color)
            match nb_color[1]:
                case "red":
                    red += int(nb_color[0])
                case "blue":
                    blue += int(nb_color[0])
                case "green":
                    green += int(nb_color[0])

        print(red, green, blue)
        if red > 12 or green > 13 or blue > 14:
            work = False
    if work:
        total += number_game
print(total)


# atempt 1 5050 to hight
# atempt 2 411 to low
# atempt 2 2176 the good one

