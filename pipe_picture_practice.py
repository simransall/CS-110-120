''' File: pipe_picture_practice.py
    Author:  Simran Sall
    Purpose: use graphics to draw a pipe grid index
        preparation for the next programming assignment
'''

from graphics import graphics

gui = graphics(600, 600, 'Pipe Grid')

def create_panels(gui):
    #left column
    gui.rectangle(0, 0, 190, 190, 'gray') #top left
    gui.rectangle(0, 200, 190, 190, 'gray') #middle left
    gui.rectangle(0, 400, 190, 200, 'gray') #bottom left

    #middle column
    gui.rectangle(200, 0, 190, 190, 'gray') #top middle
    gui.rectangle(200, 200, 190, 190, 'gray') #center
    gui.rectangle(200, 400, 190, 200, 'gray') #bottom middle

    #right column
    gui.rectangle(400, 0, 200, 190, 'gray') #top right
    gui.rectangle(400, 200, 200, 190, 'gray') #middle right
    gui.rectangle(400, 400, 200, 200, 'gray') #bottom right

def draw_pipes(gui):
    #top left
    gui.rectangle(100, 100, 20, 90, 'black')
    gui.rectangle(100, 100, 90, 20, 'black')

    #middle left
    gui.rectangle(100, 200, 20, 190, 'black')
    gui.rectangle(0, 300, 190, 20, 'black')

    #bottom left
    gui.rectangle(100, 400, 20, 120, 'black')

    #top middle
    gui.rectangle(200, 100, 190, 20, 'black')
    gui.rectangle(290, 0, 20, 100, 'black')
    gui.rectangle(270, 80, 60, 60, 'black')

    gui.rectangle(200, 105, 190, 8, 'blue')
    gui.rectangle(295, 0, 8, 105, 'blue')
    gui.rectangle(280, 90, 40, 40, 'blue')

    #center
    gui.rectangle(200, 300, 190, 20, 'black')
    gui.rectangle(200, 305, 190, 8, 'blue')

    #bottom middle
    gui.rectangle(200, 500, 190, 20, 'black')

    #middle right
    gui.rectangle(500, 200, 20, 190, 'black')
    gui.rectangle(485, 280, 50, 50, 'black')

    #bottom right
    gui.rectangle(400, 500, 200, 20, 'black')

create_panels(gui)
draw_pipes(gui)
