#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 1

time = my_file_parse[0][:-1].split(":")[1].split(" ")
time = [int(x) for x in time if x != ""]

distances = my_file_parse[1].split(":")[1].split(" ")
distances = [int(x) for x in distances if x != ""]
print("Time = ", time)
print("Distances = ", distances)

for i in range(len(time)):
    speed = 0
    distance = 0
    tmp_total = 0
    for j in range(0, time[i]):
        speed = j
        distance = speed * (time[i] - j)
        print("speed = ", speed)
        print("distance = ", distance)
        if distance > distances[i]:
            tmp_total += 1
    total *= tmp_total
    print("=" * 20)
    print("tmp_total = ", tmp_total)
    print("=" * 20)


print("Total = ", total)

# attempt 1 74698 the result
