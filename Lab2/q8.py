from LocationGraph import LocationGraph

def main():
    # Test case 1
    print("\nTest case 1\n")
    graph = LocationGraph(nodes=set('ABC'),
                          locations={'A': (0, 0),
                                     'B': (3, 0),
                                     'C': (3, 4)},
                          edges={('A', 'B'), ('B','C'),
                                 ('C', 'A')},
                          starting_nodes=['A'],
                          goal_nodes={'C'})


    for arc in graph.outgoing_arcs('A'):
        print(arc)

    for arc in graph.outgoing_arcs('B'):
        print(arc)

    for arc in graph.outgoing_arcs('C'):
        print(arc)
    
    # Test case 2
    print("\nTest case 2\n")
    pythagorean_graph = LocationGraph(
    nodes=set("abc"),
    locations={'a': (5, 6),
               'b': (10,6),
               'c': (10,18)},
    edges={tuple(s) for s in {'ab', 'ac', 'bc'}},
    starting_nodes=['a'],
    goal_nodes={'c'})

    for arc in pythagorean_graph.outgoing_arcs('a'):
        print(arc)

if __name__ == "__main__":
    main()
