def construct_perceptron(weights, bias):
    return lambda i: 1 if sum(x * w for x, w in zip(i, weights)) + bias >= 0 else 0
