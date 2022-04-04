from graphics import graphics

def main():
    gui = graphics(700, 300, 'Graphics')
    i=0
    while i < 700:
        offset = i * 50
        if i % 2 == 0:
            gui.line(offset, 50, offset, 250, 'blue', 25)
        else:
            gui.line(offset, 50, offset, 250, 'red', 25)
        i += 1

main()