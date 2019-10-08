import itertools


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    for examples in itertools.repeat(training_examples, max_epochs):
        misclassified = False
        for e_in, e_out in examples:
            a_out = 1 if sum(x * w for x, w in zip(e_in, weights)) + bias >= 0 else 0

            if a_out != e_out:
                misclassified = True
                weights = [w + learning_rate * i * (e_out - a_out) for w, i in zip(weights, e_in)]
                bias += learning_rate * (e_out - a_out)
        
        if not misclassified:
            return (weights, bias)

    return (weights, bias)
