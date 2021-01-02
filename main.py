from Shared.SearchShell import SearchShell
from art import *
import time, json
from colorit import *

Algorithms = [{"id": 1, "name": "Breadth first search"}, {"id": 2, "name": "Depth first search"},
              {"id": 3, "name": "Greedy best-first search"}, {"id": 4, "name": "A*"}]
Problems = [{"id": 1, "name": "Peg Solitaire", "heuristics": [{"id": 1, "name": "Pegs left in the table"},
                                                              {"id": 2,
                                                               "name": "Based on Similarities with the goal state"}]},
            {"id": 2, "name": "8 Puzzle",
             "heuristics": [{"id": 1, "name": "Manhattan Distance"}, {"id": 2, "name": "Displaced Tiles"}]},
            {"id": 3, "name": "Missionnaries and Cannibals",
             "heuristics": [
                 {"id": 1, "name": "Total Missionnaries and Cannibals in the right side (totalLeftHeuristic)"}]}]


# printing functions:
def printProblems():
    print(color('------- Problems -------', Colors.orange))
    for problem in Problems:
        print("{}: {} ".format(problem["name"], problem["id"]))
    print(color('-----------------------', Colors.orange))


def printAlgorithms():
    print(color('------- Algorithms -------', Colors.orange))
    for algorithm in Algorithms:
        print("{}: {} ".format(algorithm["name"], algorithm["id"]))
    print(color('-----------------------', Colors.orange))


def printHeuristics(problem):
    print(color('------- Heuristics -------', Colors.orange))
    for heuristic in Problems[problem - 1]["heuristics"]:
        print("{}: {} ".format(heuristic["name"], heuristic["id"]))
    print(color('-----------------------', Colors.orange))


def getDatafromJSON():
    with open("Files/states.json", "r") as read_file:
        data = json.load(read_file)
    return data


def printInitialStates(data):
    initialStates = data
    count = 1
    print(color('------- Initial States -------', Colors.orange))
    print(color('-------', Colors.orange))
    for initialState in initialStates:
        print("{}: {}".format(initialState, count))
        count += 1
        print(color('-------', Colors.orange))


def printGoalStates(data):
    goalStates = data
    count = 1
    print(color('------- Goal States -------', Colors.orange))
    print(color('-------', Colors.orange))
    for goalState in goalStates:
        print("{}: {}".format(goalState, count))
        count += 1
        print(color('-------', Colors.orange))


def intToProblemName(pb):
    if pb == 1:
        return "pegsolitaire"
    elif pb == 2:
        return "puzzle8"
    elif pb == 3:
        return "missionnariesandcannibals"


# name : id
def initializeShell():
    problem = 0
    algorithm = 0
    heuristic = 0
    tprint('SOLVEIT')
    aprint("happy")
    print(color("When intelligence meets puzzles.", Colors.purple))
    aprint("happy")
    print()
    printProblems()
    while problem not in range(1, 4):
        problem = int(input("Please choose the problem: "))
    jsonData = getDatafromJSON()
    initialStates = jsonData[intToProblemName(problem)]["initialStates"]
    goalStates = jsonData[intToProblemName(problem)]["goalStates"]
    printInitialStates(initialStates)
    initial = int(input("Please choose an initial State: "))
    initialState = initialStates[initial - 1]
    printGoalStates(goalStates)
    goal = int(input("Please choose a goal State: "))
    goalState = goalStates[goal - 1]
    printAlgorithms()
    while algorithm not in range(1, 5):
        algorithm = int(input("Please choose the algorithm: "))
    if algorithm >= 3:
        printHeuristics(problem)
        while heuristic not in range(1, 4):
            heuristic = int(input("Please choose the Heuristic: "))
    depthLimit = int(input("Please enter the depth limit: "))
    return SearchShell(algorithm, problem, depthLimit, initialState, goalState, heuristic)


def main():
    Shell = initializeShell()
    tic = time.perf_counter()
    Shell.run()
    toc = time.perf_counter()
    Shell.report(toc - tic)


if __name__ == "__main__":
    main()
