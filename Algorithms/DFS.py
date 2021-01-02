from colorit import *
def DFS(tree, depth_limit=0):
    depth = 0
    Solutions = []
    while not tree.frontiersIsEmpty():
        # takes last node (Stack simulation)
        node = tree.getFrontiers()[-1]
        # pause when depth limit reached
        if depth_limit != 0 and depth == depth_limit and tree.getExpansions() % depth_limit == 0:
            print("Node expand limit reached!")
            userInput = input("Do you want to continue expanding, if so type y otherwise type n: ")
            if userInput == 'n' or userInput == 'N' or userInput == 'no' or userInput == 'No':
                break
        #test goal state if true, prints solution and breaks, if you want more solutions you can remove the break from the condition
        if node.testGoalState():
            print(color("CONGRATS, WE FOUND A SOLUTION! \n",Colors.green))
            Solution = node.getSolution()
            Solution.reverse()
            print(color("------------- START SOLUTION -------------",Colors.green))
            count = 1
            for Node in Solution:
                print("Step {}: ".format(count))
                Node.printState()
                print()
                print(color("-------------",Colors.green))
                count += 1
            Solutions.append(Solution)
            print(color("------------- END SOLUTION -------------",Colors.green))
            break
        tree.popLastFrontier()
        tree.addExploredNode(node)
        tree.executeSuccessorFunction(node)
        depth += 1
