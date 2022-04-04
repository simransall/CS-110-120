from graphics import graphics

def main():
    gui = graphics (500, 300, 'Example')
    x = 0
    y = 0
    while True:
        gui.clear()
        gui.rectangle(x, y, 50, 50, 'blue')
        gui.update_frame(50)
        x+=5
        y+=5
        if x == 500:
            x -= 600
        if y == 300:
            y-=400

main()