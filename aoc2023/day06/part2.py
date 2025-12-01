#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 1

times = my_file_parse[0][:-1].split(":")[1].split(" ")
times = [int(x) for x in times if x != ""]

distances = my_file_parse[1].split(":")[1].split(" ")
distances = [int(x) for x in distances if x != ""]

total_times = 0
for time in times:
    for i in range(0, len(str(time))):
        total_times = total_times * 10
    total_times += time

total_distances = 0
for time in distances:
    for i in range(0, len(str(time))):
        total_distances = total_distances * 10
    total_distances += time

print("Times = ", total_times)
print("Distances = ", total_distances)


speed = 0
distance = 0
tmp_total = 0
for j in range(0, total_times):
    speed = j
    distance = speed * (total_times - j)
    if distance > total_distances:
        tmp_total += 1
total *= tmp_total
print("=" * 20)
print("tmp_total = ", tmp_total)
print("=" * 20)


print("Total = ", total)

# attempt 1 27563421 the result
