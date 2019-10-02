from itertools import islice
import csv


def learn_likelihood(file_name, pseudo_count=0):
    with open(file_name) as in_file:
        training_examples = [tuple(int(i) for i in row) for row in islice(csv.reader(in_file), 1, None)]
        n_spam, n_entries = sum(row[-1] for row in training_examples), len(training_examples)

        # Format = {Xn : [[Xn if SPAM = False], [Xn if SPAM = True]]
        d_vars = {n: [pseudo_count, pseudo_count] for n in range(12)}
        
        for row in training_examples:
            for n, obs in enumerate(row[:-1]):
                d_vars[n][row[-1]] += obs

        return [(val[0] / ((n_entries - n_spam) + (pseudo_count * 2)),
                val[1] / (n_spam + (pseudo_count * 2))) for val in d_vars.values()]
