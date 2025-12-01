#!/usr/bin/env python3

file = open("./input.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()

total = 100000000000000000000000000000000000


index_tab_map = -1
seed_to_soil_map = []
soil_to_fertilizer_map = []
fertilizer_to_water_map = []
water_to_light_map = []
light_to_temperature_map = []
temperature_to_humidity_map = []
humidity_to_location_map = []
tab_maps = [
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map
]

seeds = my_file_parse[0][:-1].split(":")[1][1:].split(" ")
for i in range(1, len(my_file_parse)):
    if ":" in my_file_parse[i]:
        index_tab_map += 1
    else:
        if my_file_parse[i][0].isnumeric():
            if my_file_parse[i][-1] == "\n":
                line = my_file_parse[i][:-1].split(" ")
            else :
                line = my_file_parse[i].split(" ")
            for k in range (len(line)):
                line[k] = int(line[k])
            tab_maps[index_tab_map].append(line)



for seed in seeds:
    tmp_total = int(seed)
    print("seed = ",seed)
    for map in tab_maps:
        for line in map:
            if tmp_total >= line[1] and tmp_total < line[1] + line[2]:
                print("line = ", line)
                tmp_total = line[0] + (tmp_total - line[1])
                break
        print("tmp_total = ",tmp_total)
    if tmp_total < total:
        total = tmp_total


print("Total = ", total)

# attempt 1 100 too low , idiot I have set total = 100
# attempt 2 525792406 the result
