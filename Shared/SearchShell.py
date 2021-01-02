from Algorithms import BFS, DFS, ASTAR, GREEDY
from Shared.Tree import Tree
from colorit import *

class SearchShell:
    def __init__(self, algorithm, problem, depthLimit, initialState, goalState, heuristic):
        self.__algorithm = algorithm
        self.__problem = problem
        self.__depthLimit = depthLimit
        self.__initialState = initialState
        self.__goalState = goalState
        self.__heuristic = heuristic
        self.__tree = Tree(self.__problem, self.__initialState, self.__goalState,self.__heuristic)

    def getStepCostMatrix(self):
        return self.__tree.getStepCostMatrix()
    # prints a brief report
    def report(self,time):
        loops = self.__tree.getLoops()
        expandedNodes = self.__tree.getExploredSet()
        illegalStates = self.__tree.getIllegalStates()
        print(color("loops detected: {}\n Nodes Expansions: {}\n Illegal States: {}\n Time: {} seconds ".format(loops, len(expandedNodes), illegalStates,time),Colors.green))
        print()
        if input("Would you want to display the exapnded nodes: (y for yes)") == 'y':
            print("Expanded nodes: ")
            for node in expandedNodes:
                node.printState()
                
    #runs the search algorithm
    def run(self):
        # BFS
        if self.__algorithm == 1:
            BFS.BFS(self.__tree, self.__depthLimit)
        # DFS
        elif self.__algorithm == 2:
            DFS.DFS(self.__tree, self.__depthLimit)
        # GREEDY
        elif self.__algorithm == 3:
            GREEDY.GREEDY(self.__tree, self.__depthLimit)
        # ASTAR
        elif self.__algorithm == 4:
            ASTAR.ASTAR(self.__tree, self.__depthLimit)
        # ERROR
        else:
            print("Wrong algorithm chosen")
