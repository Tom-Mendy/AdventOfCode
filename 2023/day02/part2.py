#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

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
    red = 0
    blue = 0
    green = 0
    for tmp in sub_pouch:
        nb_colors = tmp.split(",")
        for nb_color in nb_colors:
            nb_color = nb_color[1:].split(" ")
            print(nb_color)
            match nb_color[1]:
                case "red":
                    if red < int(nb_color[0]):
                        red = int(nb_color[0])
                case "blue":
                    if blue < int(nb_color[0]):
                        blue = int(nb_color[0])
                case "green":
                    if green < int(nb_color[0]):
                        green = int(nb_color[0])

        print(red, green, blue)
    total += red * blue * green
print(total)


# atempt 1 115804 to hight
# atempt 2 63700 the good one
