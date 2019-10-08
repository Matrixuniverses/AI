from accuracy import accuracy
from construct_perceptron import construct_perceptron

def main():
    # Test case 1
    print("\nTest case 1\n")

    perceptron = construct_perceptron([-1, 3], 2)
    inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
    targets = [0, 1, 1, 0]

    print(accuracy(perceptron, inputs, targets))


if __name__ == "__main__":
    main()
