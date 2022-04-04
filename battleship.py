class Board:
    def __init__(self, size):
        self.size = size
        assert self.size > 0
        self.board = [['']*size]*size
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                p = Pos(None, None)
                ship = Ship(None, None)
                self.board[i][j] = (p, ship)

    def add_ship(self, ship, position):
        name = Ship.get_name(ship)
        for i in range(0, 6):
            x = int(Pos.get_x(position))
            y = int(Pos.get_y(position))
            self.board[x][y] = name[0]
        return self.board

    def print(self):
        for i in range(self.size):
            self.board.append('.' * self.size)
        print('   +' + '--' * self.size + '-+')
        n = self.size - 1
        for i in range(self.size):
            print('{:>2}'.format(n) + ' | ' + ' '.join('.'*self.size) + ' |')
            n = n-1
        print('   +' + '--' * self.size + '-+')
        n = self.size
        i = 0
        for i in range(self.size):
            if n == 10:
                print('    ' + '  '*10 + ' 1'*(int(self.size)-10))
            n -= 1
        j = 0
        print('     ', end = '')
        for i in range(self.size):
            if i >= 10:
                if j < 10:
                    print(str(j) + ' ', end = '')
                j += 1
            else:
                print(str(i) + ' ', end = '')
        print('\n')

    def has_been_used(self, pos):
        x = Pos.get_x(pos)
        y = Pos.get_y(pos)
        assert x < size
        assert y < size
        if self.board[x][y] == '*':
            return True
        elif self.board[x][y] == 'o':
            return True
        else:
            return False

    def attempt_move(self, pos):
        pass

class Ship:
    '''represents a single ship'''
    def __init__(self, name, shape):
        self.name = name
        self.shape = shape

    def get_name(self):
        return self.name

    def set_name(self, obj):
        self.name = obj

    def is_sunk(self):
        check_board = Board.add_ship(self, ship, position)
        for i in self.shape:
            x = i[0]
            y = i[1]
            if check_board[x][y] != '*':
                return False
        return True

    def print(self):
        check_board = Board.add_ship(self)
        for i in self.shape:
            x = i[0]
            y = i[1]

class Pos:
    '''represents a single point in the 2d space'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, obj):
        self.x = obj

    def set_y(self, obj):
        self.y = obj

    def rotate(self, rot):
        assert 0 <= rot <= 3
        if rot == 0:
            return (self.x, self.y)
        if rot == 1:
            return (self.y, -(self.x))
        if rot == 2:
            return (-(self.x), -(self.y))
        if rot == 3:
            return (-(self.y), self.x)




