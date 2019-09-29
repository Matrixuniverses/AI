from greedy_descent import greedy_descent

def main():

    # Test case 1
    print("\nTest case 1\n")

    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1]

    for state in greedy_descent(4, neighbours, cost):
        print(state)

    # Test case 2
    print("\nTest case 2\n")
    
    def cost(x):
        return x**2

    def neighbours(x):
        return [x - 1, x + 1]
    
    for state in greedy_descent(-6.75, neighbours, cost):
        print(state)

if __name__ == "__main__":
    main()
