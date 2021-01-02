from Shared.Node import Node
import copy


class Puzzle8(Node):
    def __init__(self, state, goalState, stepCost=[], heuristic=1):
        super().__init__(state, goalState)
        self.__size = len(self.getState())
        self.__stepCost = stepCost
        self.__goalState = goalState
        self.__heuristic = heuristic
        self.__heuristicValue = self.calculateHeuristic()

    def getSize(self):
        return self.__size

    # adapted display since state is a 2d array
    def printState(self):
        state = self.getState()
        size = len(state)
        for i in range(size):
            for j in range(size):
                print(state[i][j], end=" ")
            print()
        print()

    # get coordinates of a given element in the goal state
    def getCoordsGoalState(self, goalState, element):
        for i in range(len(goalState)):
            for j in range(len(goalState)):
                if goalState[i][j] == element:
                    return (i, j)

    # manhattan heuristic implementation
    def manhattanHeuristic(self):
        distance = 0
        state = self.getState()
        goalState = self.getGoalState()
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] != 0:
                    goalStateCoords = self.getCoordsGoalState(goalState, state[i][j])
                    tileDistance = abs(i - goalStateCoords[0]) + abs(j - goalStateCoords[1])
                    distance += tileDistance
        return distance

    # displaced tiles heuristic implementation
    def displacedTilesHeuristic(self):
        count = 0
        state = self.getState()
        goalState = self.getGoalState()
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] != goalState[i][j]:
                    count += 1
        return count

    # Calculates heuristics
    def calculateHeuristic(self):
        count = 0
        if self.__heuristic == 1:
            count = self.manhattanHeuristic()
        elif self.__heuristic == 2:
            count = self.displacedTilesHeuristic()
        self.setHeuristicValue(count)

    # tests if actual node's state is similar to a given node's state.
    def equals(self, node):
        if self.getState() == node.getState():
            return True
        else:
            return False

    # method for testing if actual's state equals goal state
    def testGoalState(self):
        # we create a Puzzle8 node with the goalstate as an initalstate in order to use the equals() method that takes a node as argument instead of a state.
        if self.equals(Puzzle8(self.__goalState, self.__goalState)):
            return True
        else:
            return False

    # Method for generate possible moves according to 8 puzzle's rules
    def successorFunction(self):
        successorSet = []
        state = self.getState()
        size = len(state)
        for i in range(size):
            for j in range(size):
                if state[i][j] == 0:

                    # UP
                    if (i - 1 >= 0):
                        upState = copy.deepcopy(state)
                        upNode = Puzzle8(upState, self.__goalState, self.__stepCost)
                        value = upState[i - 1][j]
                        upNode.updateState(i - 1, j, 0)
                        upNode.updateState(i, j, value)
                        upNode.setPreviousNode(self)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i - 1][j]
                        upNode.incrementPathCost(stepCost)
                        successorSet.append(upNode)
                    # DOWN
                    if (i + 1 < size):
                        downState = copy.deepcopy(state)
                        downNode = Puzzle8(downState, self.__goalState, self.__stepCost)
                        value = downState[i + 1][j]
                        downNode.updateState(i + 1, j, 0)
                        downNode.updateState(i, j, value)
                        downNode.setPreviousNode(self)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i + 1][j]
                        downNode.incrementPathCost(stepCost)
                        successorSet.append(downNode)
                    # RIGHT
                    if j + 1 < size:
                        rightState = copy.deepcopy(state)
                        rightNode = Puzzle8(rightState, self.__goalState, self.__stepCost)
                        value = rightState[i][j + 1]
                        rightNode.updateState(i, j + 1, 0)
                        rightNode.updateState(i, j, value)
                        rightNode.setPreviousNode(self)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i][j + 1]
                        rightNode.incrementPathCost(stepCost)
                        successorSet.append(rightNode)
                    # LEFT
                    if j - 1 >= 0:
                        leftState = copy.deepcopy(state)
                        leftNode = Puzzle8(leftState, self.__goalState, self.__stepCost)
                        value = leftState[i][j - 1]
                        leftNode.updateState(i, j - 1, 0)
                        leftNode.updateState(i, j, value)
                        leftNode.setPreviousNode(self)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i][j - 1]
                        leftNode.incrementPathCost(stepCost)
                        successorSet.append(leftNode)

        return successorSet
