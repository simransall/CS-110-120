###
### Author: Simran Sall
### Course: CSc 110
### Description: This program is a version of chess called
###              "110 1D Chess". There are 2 Knights and 1 King
###              for each player. Both Knights and Kings move
###              left and right, and can kill other pieces and take
###              their place; this includes a player killing their
###              own pieces. The color of the last piece standing
###              (black or white) indicates if Black wins or if
###              White wins.

from graphics import graphics

W_KNIGHT = 'WKn'
W_KING   = 'WKi'
B_KNIGHT = 'BKn'
B_KING   = 'BKi'
EMPTY    = '   '
WHITE    = 'White'
BLACK    = 'Black'
LEFT     = 'l'
RIGHT    = 'r'

def is_valid_move(board, position, player):
    ''' This function determines if the player's move is valid.
It evaluates the position on the board that is chosen, and ensures
that it is in the board range and that if the player is White,
a White character is chosen (and vice versa). It takes 3 parameters:
board, position, and player.
Board parameter determines where on the board the character is.
Position determines the character that will be moved.
The player parameter is included so that the function can evaluates
if it is Black or White.'''
    # define choice as the character that is chosen on the board
    choice = board[position]
    # choice must be within the bounds of the board, also cannot choose an empty spot
    if 0 <= position and position <= 8 and choice != EMPTY:
        # if the player is WHITE, they must choose a white character
        if player == WHITE and (choice == W_KING or choice == W_KNIGHT):
            return True
        # if the player is BLACK, they must choose a black character
        elif player == BLACK and (choice == B_KING or choice == B_KNIGHT):
            return True
        else:
            return False
    else:
        return False

def move(board, position, direction):
    ''' This function takes the position parameter to determine
which player should be moved. If their choice is not empty,
then the function will determine if it is a Knight that is
to be moved or a King. It takes three parameters: board, position,
and direction.
Board parameter determines where on the board the character is.
Position determines the character that will be moved.
The direction parameter is included so that the move function can
pass it to other functions.'''
    choice = board[position]
    # choice cannot be equal to EMPTY
    if choice != EMPTY:
        # determine which move function to use
        if choice == W_KNIGHT or choice == B_KNIGHT:
            move_knight(board, position, direction)
        else:
            move_king(board, position, direction)
    else:
        return False


def move_king(board, position, direction):
    ''' This function allows the King character to move along
the board. The King will keep moving left or right as long as
there is an empty spot in front of it. If they encounter a
character, they will take that character's position, and its
original position will appear as empty. This function takes the
board, position, and direction parameter.
Board parameter determines where on the board the character is.
Position determines the character that will be moved.
Direction determines if the character will be moving left or right.'''
    #move 'position' to the left or right until it hits the opponent
    #then take the opponent's place
    i = position
    piece = board[position]
    if direction == RIGHT:
        board[position] = EMPTY
        # the next board space must be empty and the position must be within
        # the length of the board
        while board[i] == EMPTY and i < (len(board)-1):
            i += 1
        board[i] = piece
    if direction == LEFT:
        board[position] = EMPTY
        # the next board space must be empty and the position must be within
        # the length of the board
        while board[i] == EMPTY and i < (len(board)-1):
            i -= 1


def move_knight(board, position, direction):
    ''' This function allows the Knight character to move along
the board. The Knight function will either move left by two
spaces or right by two spaces. If their space lands on another
character's space, they replace that other character. This function
takes the board, position, and direction parameter.
Board parameter determines where on the board the character is.
Position determines the character that will be moved.
Direction determines if the character will be moving left or right. '''
    #move 'position' to the left or right until it hits the opponent
    #then take the opponent's place
    i = position
    piece = board[position]
    if direction == RIGHT:
        board[position] = EMPTY
        # move right two spaces if the direction is right
        board[i] = board[i + 2]
    elif direction == LEFT:
        board[position] = EMPTY
        # move left two spaces if the direction is left
        board[i] = board[i - 2]
    else:
        return False


def is_game_over(board):
    ''' This function only takes the board parameter to check
what characters are left in the board list. If the white king is not
on the board, then Black wins. If the black king is not on the
board, then White wins.'''
    if W_KING not in board:
        print('Black wins!')
        return True
    if B_KING not in board:
        print('White wins!')
        return True
    if B_KING in board and W_KING in board:
        return False
    else:
        return False

def print_board(board):
    ''' This function takes the board parameter and uses the print function to
display the 1D chess board and the characters within it. '''
    i = 0
    print('+-----------------------------------------------------+')
    while i < 9:
        print('|' + ' ' + board[i] + ' ', end='')
        i += 1
    print('|')
    print('+-----------------------------------------------------+')

def draw_board(board, gui):
    ''' Implement. '''
    #gui.rectangle(35, 105, 630, 95, 'black')
    #gui.text(175, 50, "1 Dimensional Chess", "dark green", 24)
    #gui.update_frame(40)

def main():

    # Create the canvas
    gui = graphics(700, 200, '1 Dimensional Chess')

    # This is the starting board.
    # This board variable can and should be passed to other functions
    # and changed as moves are made.
    board = [W_KING, W_KNIGHT, W_KNIGHT, EMPTY, EMPTY, EMPTY, B_KNIGHT, B_KNIGHT, B_KING]


    # White typically starts in chess.
    # This will change between WHITE and BLACK as the turns progress.
    player = WHITE

    # This variable will be updated to be True if the game is over.
    # The game is over after one of the kings dies.
    is_game_won = False

    # This loop controls the repetitive nature of the turns of the game.
    while not is_game_won:

        print_board(board)

        # Draw the board
        draw_board(board, gui)

        position = int(input(player + ' enter index:\n'))
        direction = input(player + ' enter direction (l or r):\n')

        # If the desired move is valid, then call the move function.
        # Also, change the player variable.
        if is_valid_move(board, position, player):
            if player == WHITE:
                move(board, position, direction)
                player = BLACK
            else:
                move(board, position, direction)
                player = WHITE
            is_game_won = is_game_over(board)
    draw_board(board, gui)

main()