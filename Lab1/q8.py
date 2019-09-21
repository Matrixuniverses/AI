from DFSFrontier import DFSFrontier
from search import *

def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = ExplicitGraph(nodes=set('SAG'),
                      edge_list=[('S','A'), ('S', 'G'), ('A', 'G')],
                      starting_nodes=['S'],
                      goal_nodes={'G'})

    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # Test case 2
    print("\nTest case 2\n")
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})

    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # Test case 3
    print("\nTest case 3\n")
    available_flights = ExplicitGraph(
        nodes=['Christchurch', 'Auckland',
               'Wellington', 'Gold Coast'],
        edge_list=[('Christchurch', 'Gold Coast'),
                   ('Christchurch','Auckland'),
                   ('Christchurch','Wellington'),
                   ('Wellington', 'Gold Coast'),
                   ('Wellington', 'Auckland'),
                   ('Auckland', 'Gold Coast')],
        starting_nodes=['Christchurch'],
        goal_nodes={'Gold Coast'})

    my_itinerary = next(generic_search(available_flights, DFSFrontier()), None)
    print_actions(my_itinerary)

    # Test case 4
    print("\nTest case 4\n")
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list=[('S', 'G'), ('S','A'),
                                     ('A', 'S'), ('A', 'G')],
                          starting_nodes=['S'],
                          goal_nodes={'G'})

    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

    # Test case 5
    print("\nTest case 5\n")
    graph = ExplicitGraph(nodes=['Knowledge',
                                 'Commerce',
                                 'Wisdom',
                                 'Wealth',
                                 'Happiness'],
                          edge_list=[('Knowledge', 'Wisdom'),
                                 ('Commerce', 'Wealth'),
                                 ('Happiness', 'Happiness')],
                          starting_nodes=['Commerce'],
                          goal_nodes={'Happiness'})

    solutions = generic_search(graph, DFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)

if __name__ == "__main__":
    main()

