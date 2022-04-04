'''
File Name: count_items.py
Author: Simran Sall
Course: CS120 Spring 2020
Instructor: Russ Lewis
Purpose: This program summarizes words and formats them
    to show their values from greatest to least.
'''

def main():
    file_name = input('File to scan: ')
    open_file = open(file_name, 'r')
    string_int = {}
    for line in open_file:
        i = 1
        if line[0] == '#':
            continue
        line = line.strip('\n').split()
        if len(line) == 0:
            continue
        for i in range(1, len(line)):
            line[i] = int(line[i])
            if line[0] not in string_int:
                string_int[line[0]] = line[i]
            else:
                string_int[line[0]] += line[i]
    sorted(string_int.values())
    list_order = []
    for key, value in string_int.items():
        list_order.append([value, key])
    list_order.sort(reverse = True)
    j = 0
    while j < len(list_order):
        for i in range(0, len(list_order)-1):
            if list_order[i][0] == list_order[i+1][0]:
                if list_order[i][1] > list_order[i+1][1]:
                    list_order[i][1], list_order[i+1][1] = list_order[i+1][1], list_order[i][1]
                else:
                    continue
            else:
                continue
        j += 1
    for i in list_order:
        print(str(i[1]) + ' ' + str(i[0]))

main()