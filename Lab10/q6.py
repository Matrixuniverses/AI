from learn_perceptron_parameters import *
from construct_perceptron import *


def main():
    # Test case 1
    print("\nTest case 1\n")


    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 0),
      ((1, 0), 0),
      ((1, 1), 1),
      ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, 50)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")

    perceptron = construct_perceptron(weights, bias)

    print(perceptron((0,0)))
    print(perceptron((0,1)))
    print(perceptron((1,0)))
    print(perceptron((1,1)))
    print(perceptron((2,2)))
    print(perceptron((-3,-3)))
    print(perceptron((3,-1)))

    # Test case 2
    print("\nTest case 2\n")

    weights = [2, -4]
    bias = 0
    learning_rate = 0.5
    examples = [
      ((0, 0), 0),
      ((0, 1), 1),
      ((1, 0), 1),
      ((1, 1), 0),
      ]
    max_epochs = 50

    weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, 50)
    print(f"Weights: {weights}")
    print(f"Bias: {bias}\n")


if __name__ == "__main__":
    main()
