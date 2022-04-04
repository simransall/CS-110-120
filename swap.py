'''
File Name: swap.py
Author: Simran Sall
Course: CS120 Spring 2020
Instructor: Russ Lewis
Purpose: This program takes a string that the user
    inputs and swaps it. If the string is even in length,
    it swaps the first and second half. If odd in length,
    the middle character is conserved with the outer halves
    swapped.
'''

def main():
    user_input = input('Please give a string to swap: ')
    no_space = user_input.strip()
    length_input = len(no_space)
    if length_input % 2 == 0:
        first_half, second_half = no_space[:length_input//2], no_space[length_input//2:]
        new_string = second_half + first_half
        print(new_string)
    else:
        number_middle = length_input//2
        middle_character = no_space[number_middle]
        first_half, second_half = no_space[:length_input//2], no_space[(length_input//2)+1:]
        new_string = second_half + middle_character + first_half
        print(new_string)

main()