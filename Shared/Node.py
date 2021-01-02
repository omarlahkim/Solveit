class Node:
    # CONSTRUCTOR
    def __init__(self, state, goalState):
        # ATTRIBUTS
        self.__pathCost, self.__heuristicValue, self.__stepCost, self.__state, self.__previousNode, self.__state, self.__goalState = 0, 0, 1, [], None, state, goalState
        try:
            self.__pathCost = self.__previousNode.getPathCost()
        except:
            self.__pathCost = 0

    # GETTERS
    def getPathCost(self):
        return self.__pathCost

    def getHeuristicValue(self):
        return self.__heuristicValue

    def getstepCost(self):
        return self.__stepCost

    def getState(self):
        return self.__state

    def getPreviousNode(self):
        return self.__previousNode

    def getGoalState(self):
        return self.__goalState

    # SETTERS
    def setPathCost(self, pathcost):
        self.__pathCost = pathcost

    def setHeuristicValue(self, heuristicvalue):
        self.__heuristicValue = heuristicvalue

    def setstepCost(self, stepcost):
        self.__stepCost = stepcost

    def setState(self, state):
        self.__state = state

    def setPreviousNode(self, previousNode):
        self.__previousNode = previousNode

    def updateState(self, i, j, value):
        self.__state[i][j] = value

    # METHODS
    def printInfo(self):
        return

    def printState(self):
        return

    def successorFunction(self):
        return

    def equals(self, node):
        return

    def testGoalState(self):
        return

    def calculateHeuristic(self, heuristic):
        return

    def getSolution(self):
        node = self
        solution = []
        solution.append(node)
        while node.getPreviousNode() != None:
            solution.append(node.getPreviousNode())
            node = node.getPreviousNode()
        return solution

    def incrementPathCost(self, value):
        self.__pathCost += value
