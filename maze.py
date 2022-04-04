''' File: maze.py
    Author: Simran Sall
    Purpose: to solve a maze by building a data structure
        and recursing through it to build a path to get
        through the maze
'''

class Maze:
    ''' This class represents the maze as well as how to solve it.
        It can take in a list of all the vertices in the maze, build
        a data structure around it, and can return the solution.

        The constructor initializes the edge list and builds
        a data structure for the edge list using one of the
        methods in Maze.

        The class defines several helpful methods:
            _build_maze(): uses the edge list to build a data
                structure that represents each vertex in the maze
            helper_solve(): the algorithm for solving the maze by
                using recursion
            solve(): returns the path solution to the maze
    '''
    def __init__(self, edge_list):
        ''' This method builds a dictionary to represent all of the
            vertices in the edge_list. It also initializes the
            _maze attribute with this data structure
            Param: the edge_list input that is a 2D list of strings
        '''
        self.edge_list = edge_list
        self._maze = self._build_maze(edge_list)


    def _build_maze(self, edge_list):
        ''' This method uses edge_list to build a
            dictionary representing the maze. Each key-value
            pair in the dictionary represents the connection of
            vertices in the maze
            Param: the edge_list input that is a 2D list of strings
            Return: dictionary representing the vertices and their
                    connections
        '''
        edges = {}
        for i in edge_list:
            # need to create key-value pairs that go both ways
            # ex. A --> B and also B --> A (need both pairs for
            # recursion algorithm to work)
            if i[0] in edges:
                edges[i[0]].append(i[1])
            else:
                edges[i[0]] = [i[1]]
            if i[1] in edges:
                edges[i[1]].append(i[0])
            else:
                edges[i[1]] = [i[0]]
        return edges

    def helper_solve(self, visited, src, dest, path):
        ''' This method is the algorithm used to recurse
            through the dictionary given by _build_maze. It
            keeps track of all of the vertices visited as well
            as the solution to the maze (path) by appending to
            2 different lists
            Param:  visited and path are empty lists that are
                        initialized by the solve method
                    src and dest are the names of the vertices
            Return: should return True if there is a path and False
                    if there is no path
        '''
        visited.append(src)
        path.append(src)
        # base case of if there is only one vertex
        if src == dest:
            return True
        # otherwise use recursive backtracking to go through the dictionary
        for i in self._maze[src]:
            # check so that it doesn't go into an endless loop
            if i not in visited:
                if self.helper_solve(visited, i, dest, path):
                    return True
        # remove any vertex that is not part of the solution
        path.pop()
        # case if the path is empty
        return False

    def solve(self, src, dest):
        ''' This method returns the solution of the maze with the
            help of helper_solve. If the path is empty, then this
            method will return None.
            Param: src and dest are the names of the vertices
            Return: returns an array from src to dest with src being
                    the first element and dest being the last element.
        '''
        visited = []
        path = []
        if self.helper_solve(visited, src, dest, path):
            return path
        return None
