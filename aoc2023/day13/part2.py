#!/usr/bin/env python3

def get_index_tab(row, char):
    index_tab = []
    tmp = 0
    i = 0
    tmp_row = row[:]
    while tmp != -1:
        try:
            tmp = tmp_row.index(char)
            index_tab.append(tmp)
            if i != 0:
                index_tab[i] = index_tab[i] + index_tab[i-1] + 1
            tmp_row = tmp_row[tmp+1:]
            i += 1
        except:
            tmp = -1
    return index_tab

def test(row, groups, nb_place, index_tab):
    total = 0
    if nb_place == 0:
        tmp = [len(i) for i in row.split('.') if i != '']
        if tmp == groups:
            return 1
        return 0
    row_tmp = row[:index_tab[0]] + '.' + row[index_tab[0]+1:]
    total += test(row_tmp, groups, nb_place-1, index_tab[1:])
    tmp = [len(i) for i in row.split('.') if i != '']
    row_tmp = row[:index_tab[0]] + '#' + row[index_tab[0]+1:]
    total += test(row_tmp, groups, nb_place-1, index_tab[1:])

    return total

def count_arrangements(row, groups):
    count = 0
    nb_place = row.count('?')
    index_tab = get_index_tab(row, '?')
    # print(row, groups, nb_place, index_tab)
    count = test(row, groups, nb_place, index_tab)
    print(count)
    
    return count

file = open("./exemple.txt", "r")
my_file_parse: list[str] = file.readlines()
file.close()
for i in range (0, len(my_file_parse)):
    if my_file_parse[i][-1] == "\n":
        my_file_parse[i] = my_file_parse[i][:-1]
    my_file_parse[i] = my_file_parse[i]


total = 0

for row in my_file_parse:
    row_data = row.split()
    # row_string = row_data[0] + '?' + row_data[0] + '?' + row_data[0] + '?' + row_data[0] + '?' + row_data[0]
    # groups = list(map(int, row_data[1].split(','))) * 5

    row_string = row_data[0]
    groups = list(map(int, row_data[1].split(',')))


    total += count_arrangements(row_string, groups)


print("Total :", total)


print(total)

# attempt 1 8075 the result

