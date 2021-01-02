from Shared.Node import Node
import copy


class PegNode(Node):
    def __init__(self, state, goalState=[], stepCost=[], heuristic=2):
        super().__init__(state, goalState)
        self.__availableHeuristics = [{"name": "Peg Count", "value": 1}, {"name": "", "value": 2}]
        self.__size = len(self.getState())
        self.__stepCost = stepCost
        self.__heuristic = heuristic
        self.__heuristicValue = self.calculateHeuristic(self.__heuristic)
        self.__goalState = goalState

    # getter for size of state
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

    # Peg 1 Count left in the table
    def pegsLeftHeuristic(self):
        count = 0
        state = self.getState()
        for i in range(self.__size):
            for j in range(self.__size):
                if state[i][j] == 1:
                    count += 1
        return count

    # the closest state to the goal state by differences
    def closestStateToGoalStateHeuristic(self):
        count = 0
        state = self.getState()
        goalState = self.getGoalState()
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] != goalState[i][j]:
                    count += 1
        return count

    # Calculates heuristics
    def calculateHeuristic(self, heuristic):
        count = 0
        if self.__heuristic == 1:
            count = self.pegsLeftHeuristic()
        elif self.__heuristic == 2:
            count = self.closestStateToGoalStateHeuristic()
        self.setHeuristicValue(count)

    # tests if actual node's state is similar to a given node's state.
    def equals(self, node):
        if self.getState() == node.getState():
            return True
        else:
            return False

    # method for testing if actual's state equals goal state
    def testGoalState(self):
        # we create a pegnode with the goalstate as an initalstate in order to use the equals() method that takes a node as argument instead of a state.
        if self.equals(PegNode(self.getGoalState(), self.getGoalState())):
            return True
        else:
            return False

    # Method for generate possible moves according to peg solitaire's rules
    def successorFunction(self):
        successorSet = []
        state = self.getState()
        size = len(state)
        for i in range(size):
            for j in range(size):
                if state[i][j] == 0:
                    # UP
                    if (size > i - 2) and state[i - 1][j] == 1 and state[i - 2][j] == 1:
                        upState = copy.deepcopy(state)
                        upNode = PegNode(upState, self.getGoalState(), self.__stepCost)
                        upNode.updateState(i - 2, j, 0)
                        upNode.updateState(i - 1, j, 0)
                        upNode.updateState(i, j, 1)
                        upNode.setPreviousNode(self)
                        upNode.calculateHeuristic(self.__heuristic)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i - 2][j]
                        upNode.incrementPathCost(stepCost)
                        successorSet.append(upNode)
                    # DOWN
                    if (size > i + 2) and state[i + 1][j] == 1 and state[i + 2][j] == 1:
                        downState = copy.deepcopy(state)
                        downNode = PegNode(downState, self.getGoalState(), self.__stepCost)
                        downNode.updateState(i + 2, j, 0)
                        downNode.updateState(i + 1, j, 0)
                        downNode.updateState(i, j, 1)
                        downNode.setPreviousNode(self)
                        downNode.calculateHeuristic(self.__heuristic)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i + 2][j]
                        downNode.incrementPathCost(stepCost)
                        successorSet.append(downNode)
                    # RIGHT
                    if (size > j + 2) and state[i][j + 1] == 1 and state[i][j + 2] == 1:
                        rightState = copy.deepcopy(state)
                        rightNode = PegNode(rightState, self.getGoalState(), self.__stepCost)
                        rightNode.updateState(i, j + 2, 0)
                        rightNode.updateState(i, j + 1, 0)
                        rightNode.updateState(i, j, 1)
                        rightNode.setPreviousNode(self)
                        rightNode.calculateHeuristic(self.__heuristic)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i][j + 2]
                        rightNode.incrementPathCost(stepCost)
                        successorSet.append(rightNode)
                    # LEFT
                    if (size > j - 2) and state[i][j - 1] == 1 and state[i][j - 2] == 1:
                        leftState = copy.deepcopy(state)
                        leftNode = PegNode(leftState, self.getGoalState(), self.__stepCost)
                        leftNode.updateState(i, j - 2, 0)
                        leftNode.updateState(i, j - 1, 0)
                        leftNode.updateState(i, j, 1)
                        leftNode.setPreviousNode(self)
                        leftNode.calculateHeuristic(self.__heuristic)
                        stepCost = self.__stepCost[i][j] + self.__stepCost[i][j - 2]
                        leftNode.incrementPathCost(stepCost)
                        successorSet.append(leftNode)

        return successorSet
