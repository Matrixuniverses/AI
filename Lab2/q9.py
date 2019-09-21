from search import *
from LocationGraph import LocationGraph
from LCFSFrontier import LCFSFrontier


def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A'), ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    # Test case 2
    print("\nTest case 2\n")
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('B', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})

    solution = next(generic_search(graph, LCFSFrontier()))
    print_actions(solution)

    # Test case 3
    print("\nTest case 3\n")
    pythagorean_graph = LocationGraph(
        nodes=set("abc"),
        locations={'a': (5, 6),
                   'b': (10,6),
                   'c': (10,18)},
        edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
        starting_nodes=['a'],
        goal_nodes={'c'})

    solution = next(generic_search(pythagorean_graph, LCFSFrontier()))
    print_actions(solution)


if __name__ == "__main__":
    main()
