from colorit import *
def GREEDY(tree, depth_limit=0):
    depth = 0
    Solutions = []
    while not tree.frontiersIsEmpty():
        node = tree.getFrontiers()[0]
        # pause when depth limit reached
        if depth_limit != 0 and depth == depth_limit and tree.getExpansions() % depth_limit == 0:
            print("Node expand limit reached!")
            userInput = input("Do you want to continue expanding, if so type y otherwise type n: ")
            if userInput == 'n' or userInput == 'N' or userInput == 'no' or userInput == 'No':
                break
        if node.testGoalState():
            print(color("CONGRATS, WE FOUND A SOLUTION! \n", Colors.green))
            Solution = node.getSolution()
            Solution.reverse()
            print(color("------------- START SOLUTION -------------", Colors.green))
            count = 1
            for Node in Solution:
                print("Step {}: ".format(count))
                Node.printState()
                print()
                print(color("-------------", Colors.green))
                count += 1
            Solutions.append(Solution)
            print(color("------------- END SOLUTION -------------", Colors.green))
            break

        tree.popFirstFrontier()
        tree.addExploredNode(node)
        tree.executeSuccessorFunctionGreedy(node)
        depth += 1
