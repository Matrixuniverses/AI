from n_queens_neighbours import n_queens_neighbours as neighbours

def main():
    # Test case 1
    print("\nTest case 1")

    print(neighbours((1, 2)))

    # Test case 2
    print("\nTest case 2")

    print(neighbours((1, 3, 2)))

    # Test case 3
    print("\nTest case 3")

    print(neighbours((1, 2, 3)))

    # Test case 4
    print("\nTest case 4")

    print(neighbours((1,)))

    # Test case 5
    print("\nTest case 5")

    for neighbour in neighbours((1, 2, 3, 4, 5, 6, 7, 8)):
        print(neighbour)

if __name__ == "__main__":
    main()
