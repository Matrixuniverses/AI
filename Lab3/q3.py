from ForwardDeduce import *
from search import *
from KBGraph import KBGraph
from DFSFrontier import DFSFrontier


def main():
    # Test case 1
    print("\nTest case 1\n")

    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    query = {'a'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test case 2
    print("\nTest case 2\n")

    kb = """
    a :- b, c.
    b :- d, e.
    b :- g, e.
    c :- e.
    d.
    e.
    f :- a,
         g.
    """

    query = {'a', 'b', 'd'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test case 3
    print("\nTest case 3\n")

    kb = """
    all_tests_passed :- program_is_correct.
    all_tests_passed.
    """

    query = {'program_is_correct'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
        print("The query is true.")
    else:
        print("The query is not provable.")

    # Test case 4
    print("\nTest case 4\n")

    kb = """
    a :- b.
    """

    query = {'c'}
    if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
            print("The query is true.")
    else:
            print("The query is not provable.")

if __name__ == "__main__":
    main()
