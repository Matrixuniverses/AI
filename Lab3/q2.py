from ForwardDeduce import *


def main():
    # Test case 1
    print("\nTest case 1\n")

    kb = """
    a :- b.
    b.
    """

    print(", ".join(sorted(forward_deduce(kb))))

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

    print(", ".join(sorted(forward_deduce(kb))))

    # Test case 3
    print("\nTest case 3\n")
    
    kb = ""
    print(", ".join(sorted(forward_deduce(kb))))
    
    # Test case 4
    print("\nTest case 4\n")

    kb = """
    a.
    z.
    """
    print(", ".join(sorted(forward_deduce(kb))))


    # Test case 1
    print("\nTest case 1\n")

    kb = """
    wet :- is_raining.
    wet :- sprinkler_is_going.
    wet.
    """

    print(len(forward_deduce(kb)))


if __name__ == "__main__":
    main()
