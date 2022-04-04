###
### Author: Simran Sall
### Course: CSc 110
### Description: This program prints out different shapes: an hourglass,
###              a plumbbob, and a house. Users can input what character
###              they want their house/plumbbob/hourglass to be built with,
###              as well as the length of it. The program will print out a
###              shape depending on what the user inputs.
###

#Have the program exit if the user does not input a valid shape. Refer to
#lines 69-71.
from os import _exit as exit

def upward_arrow(arrow_character):
    '''
    This function will print out the upward arrows with the variable
    that the user inputs. The user can input any character they want their
    upward arrows to consist of, and this function will use that character to
    print out the upward arrows. The parameter is arrow_character, which is
    the character that the user inputs. The parameter can be found in the main
    function (line 72).
    '''
    size = 12
    index = 1
    while index <= size:
        space = ' ' * int((size-index)/2)
        step_row = arrow_character * index
        print(space + step_row)
        index += 2

def downward_arrow(arrow_character):
    '''
    This function will print out the downward arrows with the variable
    that the user inputs. The user can input any character they want their
    downward arrows to consist of, and this function will use that character to
    print out the downward arrows. The parameter is arrow_character, which is
    the character that the user inputs. The parameter can be found in the main
    function (line 72).
    '''
    size = 12
    index = 1
    index_2 = 1
    while index <= size:
        space = ' ' * (index - index_2)
        step_row = arrow_character * (size-index)
        print(space + step_row)
        index += 2
        index_2 +=1

def row(row_height):
    '''
    The row function is dependent upon the row_height parameter (line 73). Users
    will input how long they want their row-area height to be, which will influence
    how many lines are printed for the row function. For example, if the user
    inputs 4 for row_height, the row function will print out 4 lines.
    '''
    print('|---------|\n' * row_height, end='')

def main():
    '''
    This function will have the user input their desired shape, arrow character,
    and arrow height, so that the other functions can carry-out their task and
    print the shape of the hourglass, plumbbob, or house. The main function also
    defines what exactly should be printed depending on what shape is inputted
    by the user.
    '''
    shape = input("Enter shape to display: \n")
    if shape != 'hourglass' and shape != 'plumbbob' and shape != 'house':
        print("Must enter a valid shape to display")
        exit(0)
    arrow_character  = input("Enter arrow character: \n")
    row_height = int(input("Enter row-area height: \n"))
    print()
    if shape == 'hourglass':
        row(row_height)
        downward_arrow(arrow_character)
        upward_arrow(arrow_character)
        row(row_height)
    if shape == 'plumbbob':
        upward_arrow(arrow_character)
        row(row_height)
        downward_arrow(arrow_character)
    if shape == 'house':
        upward_arrow(arrow_character)
        row(row_height)

#Call the main function
main()
