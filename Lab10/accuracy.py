def accuracy(classifier, inputs, expected_outputs):
    predictions = [classifier(i) for i in inputs]
    return 1 - (sum([p ^ e for p, e in zip(predictions, expected_outputs)]) / len(expected_outputs))
