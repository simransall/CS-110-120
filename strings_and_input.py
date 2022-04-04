'''
File Name: strings_and_input.py
Author: Simran Sall
Course: CS120 Spring 2020
Instructor: Russ Lewis
Purpose: This program takes a string an evaluates it, including
    it's length, if its uppercase or lowercase, and the
    characters the string consists of.
'''

def evaluate_first_character(input_string):
    '''The purpose of this function is to evaluate the first
    character of the string.
    input_string: the string that the user inputs that is evaluated.'''
    if input_string[0] == 'q' or input_string[0] == 'w':
        print('QWERTY')
    elif input_string[0] == 'e' or input_string[0] == 'r':
        print('QWERTY')
    elif input_string[0] == 't' or input_string[0] == 'y':
        print('QWERTY')
    elif input_string[0] == 'Q' or input_string[0] == 'W':
        print('QWERTY')
    elif input_string[0] == 'E' or input_string[0] == 'R':
        print('QWERTY')
    elif input_string[0] == 'T' or input_string[0] == 'Y':
        print('QWERTY')
    elif input_string[0] == 'u' or input_string[0] == 'i':
        print('UIOP')
    elif input_string[0] == 'o' or input_string[0] == 'p':
        print('UIOP')
    elif input_string[0].isalpha():
        print('LETTER')
    elif input_string[0].isnumeric():
        print('DIGIT')
    else:
        print('OTHER')

def main():
    input_string = input("input string: ")
    string_length = len(input_string)
    print(string_length)
    print(input_string[1])
    print(input_string[:10])
    print(input_string[-5:])
    upper_string = input_string.upper()
    print(upper_string)
    evaluate_first_character(input_string)
    number_1 = input('')
    number_2 = input('')
    product_number = int(number_1) * int(number_2)
    print(product_number)

main()
