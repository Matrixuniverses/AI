from math import sqrt

def euclidean_distance(v1, v2):
    return sqrt(sum((i1 - i2) ** 2 for i1, i2 in zip(v1, v2)))


def majority_element(labels):
    """
    WARNING: This method is unstable, and needs to be updated
    """
    return max(set(list(labels)), key=labels.count)
