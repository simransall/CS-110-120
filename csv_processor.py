###
### Author: Simran Sall
### Course: CSc 110
### Description: This program evaluates a CSV file that a user inputs. It
###              gives the minimum or maximum number of a certain column
###              that the user wants.

def convert_file(file_name, number_list):
    '''This function takes the file that the user inputs and goes through it to add all of the
    numbers in the file to a list.
    file_name: name of the file that the user inputs
    number_list: empty list in which the contents of the file will be added to
    '''
    #read through the file
    open_file = open(file_name, 'r')
    read_file = open_file.readlines()
    #append the file contents to a list
    for line in read_file:
        number = line.strip('\n').split(',')
        number_list.append(number)
    return number_list

def min_operation(column_number, number_list):
    '''This function evaluates a certain column and finds the minimum number in that column.
    column_number: the number of the column that the user wants to be evaluated.
    number_list: the list of returned values from the convert_file() function which includes
        all of the contents of the CSV file in list format.
    '''
    number_1 = 0
    minimum_number = -1
    column_number = int(column_number)-1
    #iterate through the list and get the minimum number in the column
    for i in range(0,len(number_list)):
        #evaluate if the number is an int or float
        if float(number_list[i][column_number]) == int(number_list[i][column_number].split('.')[0]):
            number_1 = int(number_list[i][column_number].split('.')[0])
        else:
            number_1 = float(number_list[i][column_number])
        #compare the numbers to determine which has the lowest value
        if i == 0:
            minimum_number = number_1
        elif number_1 < minimum_number:
            minimum_number = number_1
    print('The minimum value in column ' + str(column_number+1) + ' is: ' + str(minimum_number))

def max_operation(column_number, number_list):
    '''This function evaluates a certain column and finds the maximum number in that column.
    column_number: the number of the column that the user wants to be evaluated.
    number_list: the list of returned values from the convert_file() function which includes
        all of the contents of the CSV file in list format.
    '''
    number_1 = 0
    max_number = 0
    column_number = int(column_number)-1
    #iterate through the list and get the minimum number in the column
    for i in range(0,len(number_list)):
        #evaluate if the number is an int or float
        if float(number_list[i][column_number]) == int(number_list[i][column_number].split('.')[0]):
            number_1 = float(number_list[i][column_number].split('.')[0])
        else:
            number_1 = float(number_list[i][column_number])
        #compare the numbers to determine which has the highest value
        if number_1 > max_number:
            max_number = number_1
        else:
            max_number = max_number
    print('The maximum value in column ' + str(column_number+1) + ' is: ' + str(max_number))

def avg_operation(column_number, number_list):
    '''This function evaluates a certain column and finds the average number in that column.
    column_number: the number of the column that the user wants to be evaluated.
    number_list: the list of returned values from the convert_file() function which includes
        all of the contents of the CSV file in list format.
    '''
    number_1 = 0
    total_sum = 0
    total_numbers = 0
    column_number = int(column_number)-1
    #iterate through the list to add all the numbers in the column
    for i in range(0,len(number_list)):
        number_1 = float(number_list[i][column_number])
        total_sum += number_1
        total_numbers += 1
    #calculate the average of all numbers in the column
    average = float(total_sum/total_numbers)
    print('The average for column ' + str(column_number+1) + ' is: ' + str(average))

def main():
    file_name = input('Enter CSV file name: \n')
    column_number = input('Enter column number: \n')
    column_operation = input('Enter column operation: \n')
    number_list = []
    convert_file(file_name, number_list)
    if column_operation == 'min':
        min_operation(column_number, number_list)
    elif column_operation == 'max':
        max_operation(column_number, number_list)
    else:
        avg_operation(column_number, number_list)

main()