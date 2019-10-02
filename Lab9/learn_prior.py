from itertools import islice
import csv


def learn_prior(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [int(row[-1]) for row in islice(csv.reader(in_file), 1, None)]
        spam, samples = sum(training_examples), len(training_examples)
        # Binary domain of {0,1} thus
        return (spam + pseudo_count) / (samples + pseudo_count * 2)
