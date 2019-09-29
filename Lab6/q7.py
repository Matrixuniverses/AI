from csp import *
from generate_and_test import generate_and_test
from arc_consistent import arc_consistent

def main():
    cryptic_puzzle = CSP(
        var_domains={x: set(range(0 if x != "f" else 1, 10)) for x in "twofur"},
        constraints={
            lambda t, w, o, f, u, r: len([t, w, o, f, u, r]) == len({t, w, o, f, u, r}),
            lambda t, w, o: ((0 if w < 5 else 1) + t + t) % 10 == o,
            lambda w, o, u: ((0 if o < 5 else 1) + w + w) % 10 == u,
            lambda o, r: (o + o) % 10 == r,
            lambda f: f == 1,
            lambda t: t + t >= 10
        }
    )

    # Test case 1
    print("\nTest case 1\n")

    print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
    print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))

    # Test case 2
    print("\nTest case 2\n")

    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['r']))

    # Test case 3
    print("\nTest case 3\n")

    new_csp = arc_consistent(cryptic_puzzle)
    print(sorted(new_csp.var_domains['w']))

    # Test case 4
    print("\nTest case 4\n")

    new_csp = arc_consistent(cryptic_puzzle)
    solutions = []
    for solution in generate_and_test(new_csp):
        solutions.append(sorted((x, v) for x, v in solution.items()
                                if x in "twofur"))
    print(len(solutions))
    solutions.sort()
    print(solutions[0])
    print(solutions[5])

if __name__ == "__main__":
    main()