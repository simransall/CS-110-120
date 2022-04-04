###
### Author: Simran Sall
### Course: CSc 110
### Description: This program prints out a box with
###              hashtags inside of it. The hashtags
###              appear based on the string that the
###              user inputs. Each digit in the string
###              is represented by a new line with a
###              certain amount of hashtags to reflect
###              that digit. The layout of this program
###              has the hashtags left-aligned.
###

#the program will automatically exit if characters other than
#numbers are inputted
from os import _exit as exit
bars = (input('Enter bar string: \n'))
bars.isnumeric()
if bars.isnumeric() != True:
    print('Please enter a set of valid characters.')
    exit(0)
length = (int(len(bars)))-1
print('+---------+') #top of the box has a set width
index = 0
while index <= length:
    #single out each digit in the string and convert it to an integer:
    digit_x = int(bars[index])
    #formula for the amount of space to get the correct alignment:
    space = ' ' * (9-digit_x) #there are 9 character spaces within the box
    print('|' + '#' * (digit_x) + space + '|')
    index += 1
print("+---------+") #bottom of the box has a set width

