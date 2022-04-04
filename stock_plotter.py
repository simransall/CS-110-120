###
### Author: Simran Sall
### Course: CSc 110
### Description: This program produces a stock plot based on
###              the given inputs. Users can control whether the
###              graph has a horizontal or vertical orientation.
###              The user will also enter the stock plot input string
###              to get a visual representation of a stock performance.
###


# ask user to input if they want a horizontal or vertical mode
orientation = str(input("Enter stock plotter mode: \n"))
# the question will keep repeating until the user types the correct
# input for the function
while orientation != "horizontal" and orientation != "vertical":
    orientation = str(input("Enter stock plotter mode: \n"))
plot_drawing = str(input("Enter stock plot input string: \n"))
length = (len(plot_drawing))
# the question will keep repeating until the user types in a correct
# input that is even in length
while length % 2 != 0:
    plot_drawing = str(input("Enter stock plot input string: \n"))

if orientation == 'vertical':
    print('#' * 19) # max width of the plot
    # define the variable position so that the asterisk is correctly placed
    right = 8
    left = 8
    index = 0
    while index < length:
        if plot_drawing[index] == 'd':
            # get alignment on graph if the string indicates d
            right += int(plot_drawing[index+1])
            left -= int(plot_drawing[index+1])
            print('#' + ' ' * left + '*' + ' ' * right + '#')
        else:
            # get alignment on graph if the string indicates u
            right -= int(plot_drawing[index+1])
            left += int(plot_drawing[index+1])
            print('#' + ' ' * left + '*' + ' ' * right + '#')
        index +=2
    print('#' * 19) # max width of the plot

if orientation == 'horizontal':
    # print the top part of the graph
    print('##' + ('#'*(length//2)) + '##') #width of the plot that adjusts to the string
    index = 16
    while index >= 0:
        line = '# '
        # define the variable position so that the asterisk is correctly placed
        pos = 8
        j = 0
        while j < length: #evaluating all of the plot pairs in the string
            # magnitude refers to the integers in the inputted string
            magnitude = int(plot_drawing[j+1])
            # single out the 'u' and 'd' in the inputted plot string to evaluate
            if plot_drawing[j] == 'd':
                magnitude = -magnitude
            pos += int(magnitude)
            if index == pos:
                line+='*'
            else:
                line += ' '
            j += 2
        print(line + ' #')
        index -= 1
    print('##' + '#'*(length//2) + '##') #width of the plot that adjusts to the string