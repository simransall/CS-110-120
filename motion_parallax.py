###
### Author: Simran Sall
### Course: CSc 110
### Description: This program displays a landscape on a graphics
###              canvas. The user can move around within the landscape
###              by moving their mouse. Each time the program is run,
###              the mountains change a different color.
###

from graphics import graphics
import random

def background(gui):
    ''' This function uses the gui graphics function to
    create the background of the landscape. The background
    includes the sky and the sun. This is done by using the rectangle
    and ellipse feature. The function parameter is "gui".
    "gui": allows for different shapes to be printed
    '''
    #define the x and y coordinates so that the shape will follow the mouse (parallax feature)
    x_coord = gui.mouse_x//25
    y_coord = gui.mouse_y//25

    gui.rectangle(-100 + x_coord, -100 + y_coord, 700, 700, 'LightSkyBlue1') #defines the background/sky
    gui.ellipse(455 + x_coord, 100 + y_coord, 75, 75, 'yellow') #defines the sun in the background

def middle_mountain(gui, color_1):
    ''' This function uses the gui graphics function to
    create the middle mountain of the landscape. This is
    done by using the triangle feature. The random function is
    also used so that each time the program is run, the mountain
    is a different color. Parameters are "gui" and "color_1"
    "gui": allows for different shapes to be printed
    "color_1": gets a random color each time the program is run
    '''
    #define the x and y coordinates so that the shape will follow the mouse (parallax feature)
    #divide by a high number because these shapes are in the background and should not move as much
    x_coord = gui.mouse_x//15
    y_coord = gui.mouse_y//15
    gui.triangle(75 + x_coord, 600 + y_coord, 300 + x_coord, 200 + y_coord,\
    600 + x_coord, 700 + y_coord, color_1)

def side_mountain(gui, color_2, color_3):
    ''' This function uses the gui graphics function to
    create the side mountains of the landscape. This is
    done by using the triangle feature. The random function is
    also used so that each time the program is run, the mountains
    are a different color. Parameters are "gui","color_2", and "color_3"
    "gui": allows for different shapes to be printed
    "color_2": gets a random color each time the program is run
    "color_3": gets a random color each time the program is run
    '''
    #define the x and y coordinates so that the shape will follow the mouse (parallax feature).
    #the parallax feature is incorporated into the x and y values of the shapes
    #divide by a high number because these shapes are in the background and should not move as much
    x_coord = gui.mouse_x//15
    y_coord = gui.mouse_y//15
    gui.triangle(-200 + x_coord, 600 + y_coord, 150 + x_coord,\
    200 + y_coord, 500 + x_coord, 650 + y_coord, color_2)
    gui.triangle(250 + x_coord, 600 + y_coord, 475 + x_coord,\
    200 + y_coord, 750 + x_coord, 650 + y_coord, color_3)

def foreground(gui):
    ''' This function uses the gui graphics function to create
    the land, the trees, and the grass blades. This is done using
    the line and ellipse feature. The function parameters is "gui"
    "gui": allows for different shapes to be printed
    '''
    #Define the x and y coordinates so that the shape will follow the mouse (parallax feature).
    #The parallax feature is incorporated into the x and y values of the shapes
    x_coord = gui.mouse_x//10
    y_coord = gui.mouse_y//10
    #Add the land. Number is out of bounds of landscape size so that parallax feature looks better.
    gui.rectangle(-100 + x_coord, 450 + y_coord, 700 + x_coord,\
    700 + y_coord, 'forest green')
    i = -200
    while i < 600: #Use a while loop to get the grass blades
        gui.line(i + x_coord, 435 + y_coord, i + x_coord,\
        450 + y_coord, 'forest green')
        i+=7
    gui.line(400 + x_coord, 400 + y_coord, 400 + x_coord,\
    450 + y_coord, 'saddle brown', 15) #tree 1
    gui.ellipse(400 + x_coord, 375 + y_coord, 65, 75, 'sea green') #tree 1 leaves
    gui.line(350 + x_coord, 400 + y_coord, 350 + x_coord, 450 + y_coord, 'saddle brown', 15) #tree 2
    gui.ellipse(350 + x_coord, 375 + y_coord, 50, 60, 'orange') #tree 2 leaves
    gui.line(450 + x_coord, 400 + y_coord, 450 + x_coord, 450 + y_coord, 'saddle brown', 15) #tree 3
    gui.ellipse(450 + x_coord, 375 + y_coord, 50, 60, 'maroon') #tree 3 leaves
    i = 50
    j = 75
    while i < 375: #using a while loop to print out 5 birds
        gui.line(((i-20) + x_coord), j + y_coord, ((i+10) + x_coord), ((j+20) + y_coord), 'black')
        gui.line(((i+10) + x_coord), ((j+20) + y_coord), ((i+40) + x_coord), j + y_coord, 'black')
        i+=80
        j+=20


def cow(gui):
    ''' This function uses the gui graphics function to create
    the cow in the landscape. The line and ellipse feature are used
    to create the cow. Function parameter is "gui".
    "gui": allows for different shapes to be printed
    '''
    #define the x and y coordinates so that the shape will follow the mouse (parallax feature).
    #the parallax feature is incorporated into the x and y values of the shapes
    x_coord = gui.mouse_x//10
    y_coord = gui.mouse_y//10
    gui.line(165 + x_coord, 440 + y_coord, 140 + x_coord, 480 + y_coord, 'black', 3) #tail of cow
    #legs of the cow:
    i = 170
    j = 450
    while i < 235:
        gui.line(i + x_coord, j + y_coord, i + x_coord, (j+50) + y_coord, 'white', 10)
        i+=20
    gui.ellipse(200 + x_coord, 450 + y_coord, 100, 75, 'white') #body of cow
    gui.ellipse(200 + x_coord, 425 + y_coord, 30, 25, 'black') #spots on body of cow
    gui.ellipse(200 + x_coord, 435 + y_coord, 25, 30, 'black') #spots on body of cow
    gui.ellipse(170 + x_coord, 445 + y_coord, 20, 10, 'black') #spots on body of cow
    gui.ellipse(170 + x_coord, 450 + y_coord, 10, 10, 'black') #spots on body of cow
    gui.ellipse(190 + x_coord, 470 + y_coord, 20, 20, 'black') #spots on body of cow
    gui.ellipse(200 + x_coord, 470 + y_coord, 30, 10, 'black') #spots on body of cow
    gui.ellipse(225 + x_coord, 475 + y_coord, 15, 10, 'black') #spots on body of cow

    gui.ellipse(250 + x_coord, 430 + y_coord, 55, 55, 'white') #cow head
    gui.ellipse(245 + x_coord, 435 + y_coord, 4, 4, 'black') #eyes
    gui.ellipse(265 + x_coord, 435 + y_coord, 4, 4, 'black') #eyes
    gui.ellipse(230 + x_coord, 420 + y_coord, 20, 25, 'black') #ears
    gui.ellipse(275 + x_coord, 420 + y_coord, 20, 25, 'black') #ears
    gui.ellipse(255 + x_coord, 450 + y_coord, 30, 17, 'pink') #snout
    gui.ellipse(247 + x_coord, 450 + y_coord, 3, 3, 'black') #snout
    gui.ellipse(260 + x_coord, 450 + y_coord, 3, 3, 'black') #snout

def main():
    gui = graphics(600, 600, 'Landscape')
    #use the random function to get random colors for the mountain each time the program runs
    color_1 = gui.get_color_string((random.randint(0, 255)),
    (random.randint(0, 255)), (random.randint(0, 255))) #color 1 is for the middle mountain
    color_2 = gui.get_color_string((random.randint(0, 255)), #color 2 is for the left mountain
    (random.randint(0, 255)), (random.randint(0, 255)))
    color_3 = gui.get_color_string((random.randint(0, 255)),
    (random.randint(0, 255)), (random.randint(0, 255))) #color 3 is for the right mountain
    while True:
        gui.clear()
        background(gui)
        middle_mountain(gui, color_1)
        side_mountain(gui, color_2, color_3)
        foreground(gui)
        cow(gui)
        gui.update_frame(50)

main()