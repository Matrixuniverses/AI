from construct_perceptron import *

def main():
    # Test case 1
    print("\nTest case 1\n")

    weights = [2, -4]
    bias = 0
    perceptron = construct_perceptron(weights, bias)

    print(perceptron([1, 1]))
    print(perceptron([2, 1]))
    print(perceptron([3, 1]))
    print(perceptron([-1, -1]))




if __name__ == "__main__":
    main()
