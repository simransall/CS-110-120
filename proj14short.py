from graphics import graphics

def body(gui, head, up_body, down_body, i, j, r, k, y1, y2):
    val = True
    count = 0
    while val:
        gui.clear()
        # first person
        gui.ellipse(70, head, 40, 40, 'black')
        gui.line(70, up_body, 70, down_body, 'black', 3)
        gui.line(70, 250, i, 270, 'black', 3)
        gui.line(70, 250, r, 270, 'black', 3)
        gui.line(i, 270, j, 300, 'black', 3)
        gui.line(r, 270, k, 300, 'black', 3)

        # second person
        gui.ellipse(170, head, 40, 40, 'black')
        gui.line(170, up_body, 170, down_body, 'black', 3)
        gui.line(170, 250, i+100, 270, 'black', 3)
        gui.line(170, 250, r+100, 270, 'black', 3)
        gui.line(i+100, 270, j+100, 300, 'black', 3)
        gui.line(r+100, 270, k+100, 300, 'black', 3)

        # third person
        gui.ellipse(270, head, 40, 40, 'black')
        gui.line(270, up_body, 270, down_body, 'black', 3)
        gui.line(270, 250, i+200, 270, 'black', 3)
        gui.line(270, 250, r+200, 270, 'black', 3)
        gui.line(i+200, 270, j+200, 300, 'black', 3)
        gui.line(r+200, 270, k+200, 300, 'black', 3)

        # fourth person
        gui.ellipse(370, head, 40, 40, 'black')
        gui.line(370, up_body, 370, down_body, 'black', 3)
        gui.line(370, 250, i+300, 270, 'black', 3)
        gui.line(370, 250, r+300, 270, 'black', 3)
        gui.line(i+300, 270, j+300, 300, 'black', 3)
        gui.line(r+300, 270, k+300, 300, 'black', 3)

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
            j += 10

        r -= 5
        if r <= 75:
            r += 10

        k += 1
        if k >= 96:
            k -= 10

        gui.line(70, y1, 40, y2, 'black', 3)
        gui.line(70, y1, 100, y2, 'black', 3)
        gui.line(170, y1, 140, y2, 'black', 3)
        gui.line(170, y1, 200, y2, 'black', 3)
        gui.line(270, y1, 240, y2, 'black', 3)
        gui.line(270, y1, 300, y2, 'black', 3)
        gui.line(370, y1, 340, y2, 'black', 3)
        gui.line(370, y1, 400, y2, 'black', 3)
        count += 1
        gui.update_frame(3)
        if count == 10:
            val = False

def raise_body(gui, head, up_body, down_body, i, j, r, k, y1, y2):
    count = 0
    while True:
        gui.clear()
        # first person
        gui.ellipse(70, head, 40, 40, 'black')
        gui.line(70, up_body, 70, down_body, 'black', 3)
        gui.line(70, 250, i, 270, 'black', 3)
        gui.line(70, 250, r, 270, 'black', 3)
        gui.line(i, 270, j, 300, 'black', 3)
        gui.line(r, 270, k, 300, 'black', 3)

        # second person
        gui.ellipse(170, head, 40, 40, 'black')
        gui.line(170, up_body, 170, down_body, 'black', 3)
        gui.line(170, 250, i+100, 270, 'black', 3)
        gui.line(170, 250, r+100, 270, 'black', 3)
        gui.line(i+100, 270, j+100, 300, 'black', 3)
        gui.line(r+100, 270, k+100, 300, 'black', 3)

        # third person
        gui.ellipse(270, head, 40, 40, 'black')
        gui.line(270, up_body, 270, down_body, 'black', 3)
        gui.line(270, 250, i+200, 270, 'black', 3)
        gui.line(270, 250, r+200, 270, 'black', 3)
        gui.line(i+200, 270, j+200, 300, 'black', 3)
        gui.line(r+200, 270, k+200, 300, 'black', 3)

        # fourth person
        gui.ellipse(370, head, 40, 40, 'black')
        gui.line(370, up_body, 370, down_body, 'black', 3)
        gui.line(370, 250, i+300, 270, 'black', 3)
        gui.line(370, 250, r+300, 270, 'black', 3)
        gui.line(i+300, 270, j+300, 300, 'black', 3)
        gui.line(r+300, 270, k+300, 300, 'black', 3)

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
            j += 10

        r -= 5
        if r <= 75:
            r += 10

        k += 1
        if k >= 96:
            k -= 10

        gui.line(70, y2-50, 40, y1-50, 'purple', 3)
        gui.line(70, y2-50, 100, y1-50, 'purple', 3)
        # second person
        gui.line(170, y2-50, 140, y1-10, 'purple', 3)
        gui.line(140, y1-10, 130, y2-20, 'purple', 3)
        gui.line(170, y2-50, 200, y1-10, 'purple', 3)
        gui.line(200, y1-10, 210, y2-20, 'purple', 3)
        # third person
        gui.line(270, y1-20, 300, y1-50, 'purple', 3)
        gui.line(270, y1-20, 300, y1, 'purple', 3)
        # fourth person
        gui.line(370, y2-50, 340, y1-20, 'purple', 3)
        gui.line(370, y2-50, 400, y1-20, 'purple', 3)
        gui.line(340, y1-20, 370, y1-50, 'purple', 3)
        gui.line(400, y1-20, 370, y1-50, 'purple', 3)

        count += 1
        gui.update_frame(3)
        if count == 10:
            return

def main():
    head = 150
    up_body = 170
    down_body = 250
    i = 60
    j = 45
    r = 80
    k = 95
    y1 = 200
    y2 = 250
    time = 0
    gui = graphics(450, 300, 'Graphics')
    while True:
        gui.clear()
        body(gui, head, up_body, down_body, i, j, r, k, y1, y2)
        raise_body(gui, head, up_body, down_body, i, j, r, k, y1, y2)
        gui.update_frame(5)

if __name__ == '__main__':
    main()
