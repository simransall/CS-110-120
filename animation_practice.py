from graphics import graphics

def arms(gui):
    i = 0
    j = 0
    #while i < 2:
    #    gui.clear()
    while True:
        gui.clear()
        gui.line(70, 200, 40, 250, 'black', 1)
        gui.line(70, 200, 100, 250, 'black', 1)
        gui.update_frame(5)
    #    i += 1

    # while i is less than 2, have the arms in the priginal position
    # then move them up while j < 3
    # then while true, have them hold the ymca shapes

def body(gui):
    head = 150
    up_body = 170
    down_body = 250
    i = 60
    j = 45
    r = 80
    k = 95
    while True:
        gui.clear()
        # first person
        gui.ellipse(70, head, 40, 40, 'powder blue')
        gui.line(70, up_body, 70, down_body, 'black', 1)
        gui.line(70, 250, i, 270, 'black', 1)
        gui.line(70, 250, r, 270, 'black', 1)
        gui.line(i, 270, j, 300, 'black', 1)
        gui.line(r, 270, k, 300, 'black', 1)

        # second person
        gui.ellipse(170, head, 40, 40, 'powder blue')
        gui.line(170, up_body, 170, down_body, 'black', 1)
        gui.line(170, 250, i+100, 270, 'black', 1)
        gui.line(170, 250, r+100, 270, 'black', 1)
        gui.line(i+100, 270, j+100, 300, 'black', 1)
        gui.line(r+100, 270, k+100, 300, 'black', 1)

        # third person
        gui.ellipse(270, head, 40, 40, 'powder blue')
        gui.line(270, up_body, 270, down_body, 'black', 1)
        gui.line(270, 250, i+200, 270, 'black', 1)
        gui.line(270, 250, r+200, 270, 'black', 1)
        gui.line(i+200, 270, j+200, 300, 'black', 1)
        gui.line(r+200, 270, k+200, 300, 'black', 1)

        # fourth person
        gui.ellipse(370, head, 40, 40, 'powder blue')
        gui.line(370, up_body, 370, down_body, 'black', 1)
        gui.line(370, 250, i+300, 270, 'black', 1)
        gui.line(370, 250, r+300, 270, 'black', 1)
        gui.line(i+300, 270, j+300, 300, 'black', 1)
        gui.line(r+300, 270, k+300, 300, 'black', 1)

        head += 5
        if head >= 155:
            head -= 10

        up_body += 5
        if up_body >= 175:
            up_body -= 10

        down_body += 5
        if down_body >= 255:
            down_body -= 5

        i += 5
        if i >= 65:
            i -= 10

        j -= 1
        if j <= 44:
            j += 5

        r -= 5
        if r <= 75:
            r += 10

        k += 1
        if k >= 96:
            k -= 5

        gui.update_frame(5)

def main():
    gui = graphics(450, 300, 'Graphics')
    while True:
        gui.clear()
        body(gui)
        arms(gui)
        gui.update_frame(5)
        gui.frame_speed(10)

if __name__ == '__main__':
    main()
