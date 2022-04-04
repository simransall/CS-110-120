from moves import *

def legal_move(board, mov):
    if board[mov[0]] != '1':
        return False
    if board[mov[1]] != '1':
        return False
    if board[mov[2]] != '0':
        return False
    else:
        return True

def legal_move_interface(board_str, mov):
    board = {}
    j = 0
    for i in board_str:
        board[j] = i
        j += 1
    return legal_move(board, mov)

def all_legal_moves(size, board):
    possible_moves = []
    for i in board:
        for j in i:
            possible_moves.append(j)
    possible_moves = set(possible_moves)
    return possible_moves

def all_legal_moves_interface(size, board_str):
    board = []
    combos = all_moves(size)
    for i in combos:
        if legal_move_interface(board_str, i) is True:
            board.append([i])
    return all_legal_moves(size, board)

def update_board(board, mov):
    board[mov[0]] = '0'
    board[mov[1]] = '0'
    board[mov[2]] = '1'
    board_string = ''
    for x in board.values():
        board_string += x
    return board_string

def update_board_interface(board_str, mov):
    if legal_move_interface(board_str, mov) is True:
        board = {}
        j = 0
        for i in board_str:
            board[j] = i
            j += 1
        return update_board(board, mov)
    else:
        return False

