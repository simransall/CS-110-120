###
### Author: Simran Sall
### Course: CSc 110
### Description: This program prints out a box with
###              hashtags inside of it. The hashtags
###              appear based on the string that the
###              user inputs. Each pair of digits in
###              the string is represented by a new line
###              with a certain amount of hashtags to
###              reflect that pair of digits. The layout
###              of this program has the hashtags appear
###              to start in the center of the box, but
###              then move outward (left and right) depending
###              on the value of the left and right digit
###              in the pair.
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
print('+------------------+') #top of the box has a set width
index = 0
while index <= length:
    digit_0 = int(bars[index])
    digit_x = int(bars[index+1])
    #formula for the amount of space to get the correct alignment:
    space_0 = ' ' * (9-digit_0) #space for the left side
    space_x = ' ' * (9-digit_x) #space for the right side
    print('|' + space_0 + '#' * digit_0 + '#' * digit_x + space_x + '|')
    index += 2
print("+------------------+") #bottom of the box has a set width

