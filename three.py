###
### Author: Simran Sall
### Course: CSc 110
### Description: This program creates a basic animation of shapes that
###              move across the screen at the same speed. All three
###              shapes are aligned in a column and move at the same rate.
###              The program utilizes the graphics function and the random
###              function.
###

from graphics import graphics
import random
def main():
    '''Main function uses the draw loop to create an animation in which
    an ellipse, rectangle, and triangle move across the screen at the same rate.
    When the shapes reach the end of the canvas, the y value is reset randomly to
    appear at a different location when it wraps back around the screen.
    '''
    gui = graphics (600,600,'Three Shapes')
    x = 0
    #set a random y value so that the y position can change  every time it runs across the screen
    y_ellipse = random.randint(60,540)
    y_rectangle = random.randint(60,540)
    y_triangle = random.randint(60,540)
    while True:
        gui.clear()
        gui.ellipse(x, y_ellipse, 60, 60, 'tomato')
        gui.rectangle((x-30), y_rectangle, 65, 65, 'violet red')
        gui.triangle(x, y_triangle, (x-30), (y_triangle+65), (x+30), (y_triangle+65), 'blue')
        gui.update_frame(80)
        x += 5
        if x == 600:
            x -= 700
            #y value will change randomly when the shape is off the screen
            y_ellipse = random.randint(60,540)
            y_rectangle = random.randint(60,540)
            y_triangle = random.randint(60,540)
main()