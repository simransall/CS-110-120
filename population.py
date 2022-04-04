'''
File Name: population.py
Author: Simran Sall
Course: CS120 Spring 2020
Instructor: Russ Lewis
Purpose: This program takes a file that holds
    information about a location and its population,
    and gives a summary about it.
'''

def main():
    user_input = input('file: ')
    new_input = user_input.strip()
    population_file = open(new_input, 'r')
    state_count = 0
    population_count = 0
    i = 0
    for line in population_file:
        if line[0] == '#':
            continue
        line = line.strip('\n').split()
        if len(line) == 0:
            continue
        state_count += 1
        population_count += int(line[-1])
        i += 1
        print('State/Territory: ' + ' '.join(line[:-1]))
        print('Population: ' + line[-1])
        print()
    print('# of States/ Territories: ' + str(state_count))
    print('Total Population: ' + str(population_count))

main()