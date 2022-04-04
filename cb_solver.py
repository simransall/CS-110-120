''' File: cb_solver.py
    Author: Simran Sall
    Purpose: This program give solutions to the cracker barrel puzzle'''

from cb_utils import *

def helper_cb_one(size, config, path):
    ''' This function uses recursion to iterate through all of the possible
        moves within the board and returns a possible pathway.
        Arguments: size is the amount of rows in the puzzle
                   config is the string of 0s and 1s that represents the board
                   path is the list in which the tuples in the correct order
                    will be added to.
        Return Value: returns True if a pathway is found, False if not
        Pre-condition: none
    '''
    # determine all of the legal moves within the board
    possible_moves = all_legal_moves_interface(size, config)
    # set a variable to keep track of the amount of 1s within the string
    count = 0
    # create the base case
    if possible_moves == set():
        for j in config:
            if j == '1':
                count += 1
        # if only 1 peg on the board, then the solution has been reached
        if count == 1:
            return True
        return False
    for i in possible_moves:
        # use recursive backtracking to update the pathway and the board string
        path.append(i)
        updated_string = update_board_interface(config, i)
        if helper_cb_one(size, updated_string, path) is True:
            return True
        path.pop()
    return False

def cb_one(size, config):
    ''' Since I use a helper function to find a solution, this
        function acts as an initializer for my helper function (helper_cb_one)
        and it also returns one possible solution to the cracker barrel puzzle.
        Arguments: size is the amount of rows in the puzzle
                   config is the string of 0s and 1s that represents the board
        Return Value: a string that consists of a list of tuples that outlines
                      the correct order to solve the puzzle. It only gives one
                      possible solution
        Pre-condition: size is >=4
    '''
    path = []
    # after initializing the data structure, call the helper function
    helper_cb_one(size, config, path)
    # return the pathway that is given by the helper function
    return str(path)


def helper_cb_all(size, config, all_solutions, path):
    ''' This function uses recursion to iterate through all of the possible
        moves within the board and returns all of the possible pathways.
        Arguments: size is the amount of rows in the puzzle
                   config is the string of 0s and 1s that represents the board
                   all_solutions is the overall list in which the paths will be
                    added to
                   path is the list in which the tuples in the correct order
                    will be added to.
        Return Value: returns all_solutions, which is the list that contains
                      all possible solutions to the puzzle
        Pre-condition: none
    '''
    # determine all of the legal moves within the board
    possible_moves = all_legal_moves_interface(size, config)
    count = 0
    # create the base case
    if possible_moves == set():
        for j in config:
            if j == '1':
                count += 1
        if count == 1:
            # this means the solution has been found
            # we don't want to return otherwise we will cut the recursion short
            # and won't find all the pathways
            all_solutions.append(str(path))
    for i in possible_moves:
        # use recursive backtracking to update the pathway and the board string
        path.append(i)
        updated_string = update_board_interface(config, i)
        helper_cb_all(size, updated_string, all_solutions, path)
        path.pop()
    return all_solutions

def cb_all(size, config):
    '''Since I use a helper function for the recursion to find a solution, this
        function acts as an initializer for my helper function (helper_cb_all)
        and it also returns all possible solutions to the puzzle.
        Arguments: size is the amount of rows in the puzzle
                   config is the string of 0s and 1s that represents the board
        Return Value: a set that consists of 1 or more pathways that outlines
                      the correct order to solve the puzzle. It gives all
                      possible solutions to the puzzle
        Pre-condition: size is >=4
    '''
    all_solutions = []
    path = []
    # after initializing the data structures, call the helper function
    helper_cb_all(size, config, all_solutions, path)
    # return the pathways that are given by the helper function
    return set(all_solutions)

