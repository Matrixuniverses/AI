from BFSFrontier import BFSFrontier
from search import *

def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = ExplicitGraph(nodes=set('SAG'),
                          edge_list = [('S','A'), ('S', 'G'), ('A', 'G')],
                          starting_nodes = ['S'],
                          goal_nodes = {'G'})

    solutions = generic_search(graph, BFSFrontier())
    solution = next(solutions, None)
    print_actions(solution)
    
    # Test case 2
    print("\nTest case 2\n")
    flights = ExplicitGraph(nodes=['Christchurch', 'Auckland', 
                                   'Wellington', 'Gold Coast'],
                            edge_list = [('Christchurch', 'Gold Coast'),
                                     ('Christchurch','Auckland'),
                                     ('Christchurch','Wellington'),
                                     ('Wellington', 'Gold Coast'),
                                     ('Wellington', 'Auckland'),
                                     ('Auckland', 'Gold Coast')],
                            starting_nodes = ['Christchurch'],
                            goal_nodes = {'Gold Coast'})

    my_itinerary = next(generic_search(flights, BFSFrontier()), None)
    print_actions(my_itinerary)

if __name__ == "__main__":
    main()
