''' File: pipegrid.py
    Author: Simran Sall
    Purpose: Takes information and formats it in a way to model
    a Pipe Grid using graphics as well as be able to change
    the orientation of the pipes and water flow
'''

class Pipes:
    '''This class creates the Pipe Grid using the individual details
    of the input list-of-lists that represents a grid.
    '''
    def __init__(self, grid, square_size):
        '''This constructor function creates instances of the grid
        and square size object
        '''
        self.grid = grid
        self.square_size = square_size

    def draw(self):
        '''This function draws out the pipe grid. I wanted
        to use the second class to draw out the actual pipes
        but was not able to implement it successfully
        '''
        from graphics import graphics
        wid = Pipes.get_wid(self)
        hei = Pipes.get_hei(self)
        size = self.square_size * hei
        gui = graphics(size, size, 'Pipe Grid')
        i = size//wid
        j = size//hei
        k = i-10 # this will act as the second pair of coordinates for each cell
        count = 0
        while count < wid:
            # create the cells of the Pipe Grid
            gui.rectangle(0, 0, k, k, 'gray')
            gui.rectangle(0, j, k, k, 'gray')
            gui.rectangle(0, j*2, k, k, 'gray')
            gui.rectangle(0, j*3, k, k, 'gray')
            gui.rectangle(0, j*4, k, k, 'gray')
            while j <= size:
                gui.rectangle(j, 0, k, k, 'gray')
                gui.rectangle(j, i, k, k, 'gray')
                gui.rectangle(j, i*2, k, k, 'gray')
                gui.rectangle(j, i*3, k, k, 'gray')
                gui.rectangle(j, i*4, k, k, 'gray')
                j += size//hei
            count += 1
        # unsuccessful attempt to draw pipes into pipe grid
        pipe = Grid.draw_pipes(self)

        gui.mainloop()

    def get_wid(self):
        '''This function returns the width of the pipe grid
        by counting the amount of individual cells there are
        within each row.
        '''
        # keep track of the width count
        wid = 0
        j = 0
        for i in self.grid:
            while j < len(i):
                wid += 1
                j += 1
        return wid

    def get_hei(self):
        '''This function returns the height of the pipe
        grid by counting the amount of rows there are total
        '''
        # keep track of the height count
        hei = 0
        for i in self.grid:
            hei += 1
        return hei

    def get_square_size(self):
        '''This function determines the square_size, or
        how many pixels the graphics window should be.
        '''
        return self.square_size

    def set_square_size(self, new_val):
        '''This function changes the square_size, or
        changes how many pixels the graphics window is.
        '''
        self.square_size = new_val
        return self.square_size

    def set_fill_state(self, x, y, state):
        '''This function determines if the individual cell
        in the pipe grid is filled with water or is not filled.
        It is filled if the state is True, otherwise it is False
        '''
        if state is True:
            # consider if it is already filled
            if '(f)' in self.grid[y][x]:
                return self.grid[y][x]
            # otherwise add that it is filled
            else:
                new = self.grid[y][x] = self.grid[y][x] +'(f)'
                return new
        else:
            not_fill = self.grid[y][x] = (self.grid[y][x]).strip('(f)')
            return not_fill

    def rotate_cw(self, x, y):
        '''This function contributes to the animation
        component of this program by changing the orientation
        of the cells clockwise
        '''
        if 'e' in self.grid[y][x]:
            self.grid[y][x].replace('e', 's')
        if 'w' in self.grid[y][x]:
            self.grid[y][x].replace('w', 'n')
        if 'n' in self.grid[y][x]:
            self.grid[y][x].replace('n', 'e')
        if 's' in self.grid[y][x]:
            self.grid[y][x].replace('s', 'w')

    def rotate_ccw(self, x, y):
        '''This function contributes to the animation
        component of this program by changing the orientation
        of the cells counter clockwise
        '''
        if 'e' in self.grid[y][x]:
            self.grid[y][x].replace('e', 'n')
        if 'w' in self.grid[y][x]:
            self.grid[y][x].replace('w', 's')
        if 'n' in self.grid[y][x]:
            self.grid[y][x].replace('n', 'w')
        if 's' in self.grid[y][x]:
            self.grid[y][x].replace('s', 'e')

    def get_cell(self, x, y):
        '''This function gathers information about
        an individual cell and returns it as a string
        '''
        self.x = x
        self.y = y
        value = self.grid[y][x]
        return value

class Grid:
    ''' Intention was to organize the information within the 2D list
    about how to construct each cell in the Pipe Grid. Intention for
    this list was to also draw the individual pipes in each cell.
    Unsuccessful attempt.
    '''

    def __init__(self, grid):
        ''' This function creates instances of the grid object.
        '''
        self.grid = grid

    def input_grid(self):
        ''' This function should gather information about each
        individual cell and pass it to the Pipes class for those
        functions to use
        '''
        for i in self.grid:
            for j in i:
                cell = j
        return cell

    def draw_pipes(self):
        ''' This function should draw the individual pipes in each
        cell within the pipe grid
        '''
        from graphics import graphics
        wid = Pipes.get_wid(self)
        hei = Pipes.get_hei(self)
        x = self.square_size//wid
        y = self.square_size//hei
        for line in self.grid:
            for cell in line:
                if '(f)' in cell:
                    color = 'blue'
                else:
                    color = 'black'
                # algorithm does not work, but I was trying to
                # come up with a pattern so it would draw it
                # a certain way if it was e, w, n, s
                if 'e' in cell:
                    gui.rectangle(x/2, y/2, x/2-10, 20, color)
                if 'w' in cell:
                    gui.rectangle(0, y/2, x/2, 20, color)
                if 'n' in cell:
                    gui.rectangle(x/2, 0, 20, y/2, color)
                if 's' in cell:
                    gui.rectangle(x/2, y/2, 20, y/2-10, color)
                if '+' in cell:
                    gui.rectangle(x/2-20, y/2-20, 50, 50, color)
                x += self.square_size//wid
                y += self.square_size//hei
