###
### Author: Simran Sall
### Course: CSc 110
### Description: This program takes a file's contents and
###              encrypts it, or puts it in a random order,
###              so it cannot be understood. It does this
###              by rearranging the lines so the entire
###              file's contents are out of order.
###


import random

def algorithm(encrypted_file, index_file, lines, index_lines, line_count):
    '''This function defines the algorithm that will rearrange the contents
    of the file. The algorithm starts off by defining 2 random numbers and
    then using those random numbers to rearrange the values in the file. It
    then appends those rearranged values to the encrypted text file.
    encrypted_file: the file in which the values of lines gets appended to.
    index_file: the file in which the values of index_lines gets appended to.
    lines: reads each line of the file that is to be encrypted.
    index_lines: empty list that is created for the line numbers of the
        rearranged lines to be added to.
    line_count: the length of the lines; used to get random numbers.
    '''
    i = 0
    for line in range(line_count*5):
        #define 2 random numbers and use those random numbers to rearrange the values in the file.
        random_1 = random.randint(0,line_count-1)
        random_2 = random.randint(0,line_count-1)
        #rearrange the values
        lines[random_1], lines[random_2] = lines[random_2], lines[random_1]
        index_lines[random_1], index_lines[random_2] = index_lines[random_2], index_lines[random_1]
    while i < (line_count):
        #append the rearranged values to the encrypted text file and index text file.
        encrypted_file.write(lines[i])
        index_file.write(str(index_lines[i])+'\n')
        i += 1
    encrypted_file.close()
    index_file.close()

def main():
    random.seed(125)
    #open the file that is to be encrypted
    file_name = input('Enter a name of a text file to encrypt: ')
    print()
    file = open(file_name, 'r')
    #open the encrypted file and index file so the encrypted contents can be added to it
    encrypted_file = open('encrypted.txt', 'w')
    index_file = open('index.txt', 'w')
    lines = file.readlines()
    index_lines = []
    for i in range(1, len(lines)+1):
        index_lines.append(i)
    line_count = len(lines)
    algorithm(encrypted_file, index_file, lines, index_lines, line_count)

main()