from Problems.PEGSOLITAIRE import PegNode
from Problems.PUZZLE8 import Puzzle8
from Problems.MissCann import MissCann
import copy, random
from colorit import *


class Tree:
    def __init__(self, problem, initialState, goalState, heuristic=1):
        self.__initialState = initialState
        self.__exploredSet = []
        self.__frontiers = []
        self.__loops = 0
        self.__expansions = 0
        self.__goalState = goalState
        self.__problem = problem
        self.__heuristic = heuristic
        self.__illegalStates = 0
        # Problem 1 is Peg Solitaire
        if self.__problem == 1:
            self.__stepCostMatrix = self.generateStepCostsPeg()
            self.__initialNode = PegNode(self.__initialState, self.__goalState, self.__stepCostMatrix, self.__heuristic)
        # Problem 2 is 8 puzzle
        elif self.__problem == 2:
            self.__stepCostMatrix = self.generateStepCostsPuzz()
            self.__initialNode = Puzzle8(self.__initialState, self.__goalState, self.__stepCostMatrix, self.__heuristic)
        # Problem 3 is Missionnaries and Cannibals
        elif self.__problem == 3:
            self.__stepCostMatrix = self.generateStepCostsMissCann()
            self.__initialNode = MissCann(self.__initialState, self.__goalState, self.__stepCostMatrix,
                                          self.__heuristic)
        else:
            print("Please choose a valid problem")
        self.__frontiers.append(self.__initialNode)

    # GETTERS
    def getFrontiers(self):
        return self.__frontiers

    def getExploredSet(self):
        return self.__exploredSet

    def getInitialNode(self):
        return self.__initialNode

    def getInitialState(self):
        return self.__initialState

    def getExpansions(self):
        return self.__expansions

    def getLoops(self):
        return self.__loops

    def getStepCostMatrix(self):
        return self.__stepCostMatrix

    def getIllegalStates(self):
        return self.__illegalStates

    # SETTERS
    def setFrontiers(self, frontiers):
        self.__frontiers = frontiers

    def setExploredSet(self, exploredSet):
        self.__exploredSet = exploredSet

    def setInitialNode(self, initialNode):
        self.__initialNode = initialNode

    def setInitialState(self, initialState):
        self.__initialState = initialState

    # METHODS
    def addFrontier(self, node):
        self.__frontiers.append(node)

    # adds node to frontier and sorts the array to get node with least heuristic value as first element
    def addFrontierGreedy(self, node):
        self.__frontiers.append(node)
        print(node.getHeuristicValue())
        self.__frontiers.sort(key=lambda node: node.getHeuristicValue())

    # adds node to frontier and sorts the array to get node with least total heuristic value as first element
    def addFrontierAstar(self, node):
        self.__frontiers.append(node)
        self.__frontiers.sort(key=lambda node: node.getHeuristicValue() + node.getPathCost())

    # adds a node to exploredSet
    def addExploredNode(self, exploredNode):
        self.__exploredSet.append(exploredNode)

    # checks if node exists in exploredSet
    def nodeExistsinExploredSet(self, node):
        for Node in self.__exploredSet:
            if node.equals(Node):
                return True
        return False

    # increments number if loops by 1
    def loopDetected(self):
        self.__loops += 1
        print("Loop detected")

    # call to execute successor function, and add the resulted nodes to frontiers set if the node has not been already expanded, otherwise number of loops is incremented by 1.
    def executeSuccessorFunction(self, node):
        successorSet = node.successorFunction()
        if len(successorSet) == 0:
            self.__illegalStates += 1
            print(color("Illegal State Detected!", Colors.blue))
        for Node in successorSet:
            if self.nodeExistsinExploredSet(Node) == False:
                print(color("-------- Added to frontier ----------", Colors.yellow))
                self.addFrontier(Node)
                Node.printState()
                print(color("------------------------------", Colors.yellow))
            else:
                print(color("-------- Loop state ----------", Colors.red))
                Node.printState()
                self.loopDetected()
                print(color("------------------------------", Colors.red))

    # call to execute successor function, and add the resulted nodes to frontiers set if the node has not been already expanded, otherwise number of loops is incremented by 1.
    def executeSuccessorFunctionGreedy(self, node):
        successorSet = node.successorFunction()
        if len(successorSet) == 0:
            self.__illegalStates += 1
            print(color("Illegal State Detected!", Colors.blue))
        for Node in successorSet:
            if self.nodeExistsinExploredSet(Node) == False:
                print(color("-------- Added to frontier ----------", Colors.yellow))
                self.addFrontierGreedy(Node)
                Node.printState()
                print(color("------------------------------", Colors.yellow))
            else:
                print(color("-------- Loop state ----------", Colors.red))
                Node.printState()
                self.loopDetected()
                print(color("------------------------------", Colors.red))

    # call to execute successor function, and add the resulted nodes to frontiers set if the node has not been already expanded, otherwise number of loops is incremented by 1.
    def executeSuccessorFunctionAstar(self, node):
        successorSet = node.successorFunction()
        if len(successorSet) == 0:
            self.__illegalStates += 1
            print(color("Illegal State Detected!", Colors.blue))
        for Node in successorSet:
            if self.nodeExistsinExploredSet(Node) == False:
                print(color("-------- Added to frontier ----------", Colors.yellow))
                self.addFrontierAstar(Node)
                Node.printState()
                print(color("------------------------------", Colors.yellow))
            else:
                print(color("-------- Loop state ----------", Colors.red))
                Node.printState()
                self.loopDetected()
                print(color("------------------------------", Colors.red))

    # increment expansions
    def newExpansion(self):
        self.__expansions += 1

    # check frontier if empty
    def frontiersIsEmpty(self):
        if len(self.__frontiers) == 0:
            return True
        else:
            return False

    # remove first element of array (Queue simulation)
    def popFirstFrontier(self):
        self.__frontiers.pop(0)

    # remove last element of array (Stack simulation)
    def popLastFrontier(self):
        self.__frontiers.pop(len(self.__frontiers) - 1)

    # adapted display when state is a 2d array
    def printGoalState(self):
        state = self.__goalState
        size = len(state)
        for i in range(size):
            for j in range(size):
                print(state[i][j], end=" ")
            print()
        print()

    # method for generating a matrix with random values as step costs for each move
    def generateStepCostsPuzz(self):
        matrix = copy.deepcopy(self.__initialState)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                # Random value between 1 and 10
                matrix[i][j] = random.randrange(1, 11)
        return matrix

    # method for generating a matrix with random values as step costs for each move
    def generateStepCostsPeg(self):
        matrix = copy.deepcopy(self.__initialState)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] != "X":
                    # Random value between 1 and 10
                    matrix[i][j] = random.randrange(1, 11)
        return matrix

    # method for generating stepcost with random values for each possible move.
    def generateStepCostsMissCann(self):
        possible = [[1, 1], [1, 0], [0, 1], [2, 0], [0, 2]]
        rules = {}
        for j in range(len(possible)):
            # Random value between 1 and 10
            rules[str(possible[j])] = random.randrange(1, 11)
        return rules
