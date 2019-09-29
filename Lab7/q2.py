from n_queens_neighbours import n_queens_cost as cost

def main():
    # Test case 1
    print("\nTest case 1\n") 

    print(cost((1, 2)))

    # Test case 2
    print("\nTest case 2\n") 

    print(cost((1, 3, 2)))

    # Test case 3
    print("\nTest case 3\n") 

    print(cost((1, 2, 3)))

    # Test case 4
    print("\nTest case 4\n") 

    print(cost((1,)))

    # Test case 5
    print("\nTest case 5\n") 

    print(cost((1, 2, 3, 4, 5, 6, 7, 8)))

    # Test case 6
    print("\nTest case 6\n") 
    
    print(cost((2, 3, 1, 4)))

if __name__ == "__main__":
    main()
