def build_rect(wid, hei):
    '''This function returns a data structure that represents a
    rectangular grid that is of a certain size. The grid consists
    of characters
    Arguments: wid is the grid width, hei is the grid height.
    '''
    assert wid >= 3
    assert hei >= 3

    width = int(wid-1)
    height = int(hei-1)
    outer_grid = []

    for i in range(wid):
        inner_grid = []
        for j in range(hei):
            inner_grid.append(' ')
        outer_grid.append(inner_grid)

    for i in range(1, height):
        for j in range(len(outer_grid[i])):
            if j == width:
                outer_grid[i][j] = 'R'
            elif j == 0:
                outer_grid[i][j] = 'L'
            else:
                outer_grid[i][j] = '.'

    for i in range(0, wid):
        for j in range(hei):
            if i == 0:
                if j != 0 and j != -1:
                    outer_grid[i][j] = 'T'
                else:
                    outer_grid[i][j] = ' '
            elif i == -1:
                if j != 0 and j != -1:
                    outer_grid[i][j] = 'B'

    return outer_grid

def print_rect(data):
    '''This function prints out the rectangular  grid.
    "any printable character is legal including space
    except for a newline character'''

    for i in data:
        for j in i:
            print(j, end=' ')
        print()

def update(data, x,y, c):
