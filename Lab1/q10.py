from search import *
from collections import deque
from itertools import dropwhile
from BFSFrontier import BFSFrontier
from FunkyNumericGraph import FunkyNumericGraph

def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = FunkyNumericGraph(4)
    for node in graph.starting_nodes():
        print(node)
    
    # Test case 2
    print("\nTest case 2\n")
    graph = FunkyNumericGraph(4)
    for arc in graph.outgoing_arcs(7):
        print(arc)
    
    # Test case 3
    print("\nTest case 3\n")
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))
    print()
    print_actions(next(solutions))

    # Test case 4
    print("\nTest case 4\n")
    graph = FunkyNumericGraph(3)
    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(dropwhile(lambda path: path[-1].head <= 10, solutions)))

if __name__ == "__main__":
    main()
