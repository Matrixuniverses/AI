from query import query

def main():
    # Test case 1
    print("\nTest case 1\n")

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.2
            }},
    }

    answer = query(network, 'A', {})
    print("P(A=true) = {:.5f}".format(answer[True]))
    print("P(A=false) = {:.5f}".format(answer[False]))

    # Test case 2
    print("\nTest case 2\n")

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    answer = query(network, 'B', {'A': False})
    print("P(B=true|A=false) = {:.5f}".format(answer[True]))
    print("P(B=false|A=false) = {:.5f}".format(answer[False]))

    # Test case 3
    print("\nTest case 3\n")

    network = {
        'A': {
            'Parents': [],
            'CPT': {
                (): 0.1
            }},

        'B': {
            'Parents': ['A'],
            'CPT': {
                (True,): 0.8,
                (False,): 0.7,
            }},
    }

    answer = query(network, 'B', {})
    print("P(B=true) = {:.5f}".format(answer[True]))
    print("P(B=false) = {:.5f}".format(answer[False]))

    # Test case 4
    print("\nTest case 4\n")

    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': ['Burglary', 'Earthquake'],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }

    answer = query(network, 'Burglary', {'John': True, 'Mary': True})
    print("Probability of a burglary when both\n"
          "John and Mary have called: {:.3f}".format(answer[True]))

    # Test case 5
    print("\nTest case 5\n")

    network = {
        'Burglary': {
            'Parents': [],
            'CPT': {
                (): 0.001
            }},

        'Earthquake': {
            'Parents': [],
            'CPT': {
                (): 0.002,
            }},
        'Alarm': {
            'Parents': ['Burglary', 'Earthquake'],
            'CPT': {
                (True, True): 0.95,
                (True, False): 0.94,
                (False, True): 0.29,
                (False, False): 0.001,
            }},

        'John': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},

        'Mary': {
            'Parents': ['Alarm'],
            'CPT': {
                (True,): 0.7,
                (False,): 0.01,
            }},
    }

    answer = query(network, 'John', {'Mary': True})
    print("Probability of John calling if\n"
          "Mary has called: {:.5f}".format(answer[True]))


if __name__ == "__main__":
    main()
