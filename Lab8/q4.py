from query import query

def main():
    network = {
        'Virus': {
            'Parents': [],
            'CPT': {
                (): 0.01
            }},

        'A': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.95,
                (False,): 0.1,
            }},

        'B': {
            'Parents': ['Virus'],
            'CPT': {
                (True,): 0.9,
                (False,): 0.05,
            }},
    }

    # Test case 1
    print("\nTest case 1\n")

    answer = query(network, 'Virus', {'A': True})
    print("The probability of carrying the virus\n"
          "if test A is positive: {:.5f}"
          .format(answer[True]))

    # Test case 2
    print("\nTest case 2\n")

    answer = query(network, 'Virus', {'B': True})
    print("The probability of carrying the virus\n"
          "if test B is positive: {:.5f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()