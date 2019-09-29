from csp import *
from arc_consistent import arc_consistent

def main():
    # Test case 1
    print("\nTest case 1\n")

    simple_csp = CSP(
        var_domains={x: set(range(1, 5)) for x in 'abc'},
        constraints={
            lambda a, b: a < b,
            lambda b, c: b < c,
            })

    csp = arc_consistent(simple_csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))


    # Test case 2
    print("\nTest case 2\n")

    csp = CSP(var_domains={x: set(range(10)) for x in 'abc'},
              constraints={lambda a, b, c: 2 * a + b + 2 * c == 10})

    csp = arc_consistent(csp)
    for var in sorted(csp.var_domains.keys()):
        print("{}: {}".format(var, sorted(csp.var_domains[var])))


if __name__ == "__main__":
    main()