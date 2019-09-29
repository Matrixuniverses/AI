from query import query

def main():
    network = {
        'Disease': {
            'Parents': [],
            'CPT': {
                (): 0.00001
            }},

        'Test': {
            'Parents': ['Disease'],
            'CPT': {
                (True,): 0.99,
                (False,): 0.01,
            }},
    }

    # Test case 1
    print("\nTest case 1\n")

    answer = query(network, 'Disease', {'Test': True})
    print("The probability of having the disease\n"
          "if the test comes back positive: {:.8f}"
          .format(answer[True]))

    # Test case 2
    print("\nTest case 2\n")

    answer = query(network, 'Disease', {'Test': False})
    print("The probability of having the disease\n"
          "if the test comes back negative: {:.8f}"
          .format(answer[True]))


if __name__ == "__main__":
    main()
