from Shared.Node import Node
import copy


class MissCann(Node):
    def __init__(self, state, goalState, stepCost=1, heuristic=1):
        super().__init__(state, goalState)
        self.__stepCost = stepCost
        self.__size = len(self.getState())
        self.__goalState = goalState
        self.__heuristic = heuristic

    # getter for state size
    def getSize(self):
        return self.__size

    # displays state
    def printState(self):
        state = self.getState()
        print(', '.join(str(element) for element in state))

    # Total Missionnaries and Cannibals in the right side
    def totalLeftHeuristic(self):
        return self.missonnaries(self.getState()) + self.cannibals(self.getState())

    # Calculates heuristics
    def calculateHeuristic(self, heuristic):
        if heuristic == 1:
            self.setHeuristicValue(self.totalLeftHeuristic())


    # tests if actual node's state is similar to a given node's state.
    def equals(self, node):
        if self.getState() == node.getState():
            return True
        else:
            return False

    # method for testing if actual's state equals goal state
    def testGoalState(self):
        # we create a MissCann node with the goalstate as an initalstate in order to use the equals() method that takes a node as argument instead of a state.
        if self.equals(MissCann(self.__goalState, self.__goalState)):
            return True
        else:
            return False

    # Method for generate possible moves according to missionnaries and cannibals's rules
    def successorFunction(self):
        successorSet = []
        possible = [[1, 1], [1, 0], [0, 1], [2, 0], [0, 2]]
        state = self.getState()
        stateCopy = None
        temporaryState = copy.deepcopy(state)
        if self.boat(temporaryState) == 1:
            for move in possible:
                temporaryState = copy.deepcopy(state)
                illegal = False
                for i in range(2):
                    temporaryState[i] -= move[i]
                    if temporaryState[i] < 0:
                        illegal = True
                    if i == 1:
                        stateCopy = copy.deepcopy(temporaryState)
                        stateCopy[2] -= 1
                        if self.missonnaries(temporaryState) >= self.cannibals(temporaryState):
                            pass
                        else:
                            illegal = True
                if illegal == False:
                    Node = MissCann(stateCopy, self.__goalState, self.__stepCost)
                    Node.setPreviousNode(self)
                    Node.calculateHeuristic(self.__heuristic)
                    stepCost = self.__stepCost[str(move)]
                    Node.incrementPathCost(stepCost)
                    successorSet.append(Node)

        elif self.boat(temporaryState) == 0:
            for move in possible:
                temporaryState = copy.deepcopy(state)
                illegal = False

                for i in range(2):
                    temporaryState[i] += move[i]

                    if temporaryState[i] > 3:
                        illegal = True
                    if i == 1:
                        stateCopy = copy.deepcopy(temporaryState)
                        stateCopy[2] += 1
                        missonnariesInLeftSide = 3 - self.missonnaries(stateCopy)
                        cannibalsInLeftSide = 3 - self.cannibals(stateCopy)
                        if self.missonnaries(stateCopy) >= self.cannibals(stateCopy) and (
                                missonnariesInLeftSide >= cannibalsInLeftSide or (
                                missonnariesInLeftSide == 0 or cannibalsInLeftSide == 0)):
                            pass
                        else:
                            illegal = True

                if illegal == False:
                    Node = MissCann(stateCopy, self.__goalState, self.__stepCost)
                    Node.setPreviousNode(self)
                    Node.calculateHeuristic(self.__heuristic)

                    stepCost = self.__stepCost[str(move)]
                    Node.incrementPathCost(stepCost)
                    successorSet.append(Node)
        return successorSet

    # get number of missionnaries on right side
    def missonnaries(self, table):
        return table[0]

    # get number of cannibals on right side
    def cannibals(self, table):
        return table[1]

    # boat value on rights side
    def boat(self, table):
        return table[2]
