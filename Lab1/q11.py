from search import *
from SlidingPuzzleGraph import SlidingPuzzleGraph
from BFSFrontier import BFSFrontier
import copy


def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = SlidingPuzzleGraph([[1, 2, 5],
                                [3, 4, 8],
                                [6, 7, ' ']])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    # Test case 2
    print("\nTest case 2\n")
    graph = SlidingPuzzleGraph([[3,' '],
                                [1, 2]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))

    # Test case 3
    print("\nTest case 3\n")
    graph = SlidingPuzzleGraph([[1, ' ', 2],
                            [6,  4,  3],
                            [7,  8,  5]])

    solutions = generic_search(graph, BFSFrontier())
    print_actions(next(solutions))


if __name__ == "__main__":
    main()
