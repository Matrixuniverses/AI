def knn_predict(input, examples, distance, combine, k):
    neighbours = sorted(((distance(input, ex[0]), ex[1]) for ex in examples), key=lambda x: x[0])

    selected, neighbours = neighbours[:k], neighbours[k:]
    
    for unselected in neighbours:
        if unselected[0] == selected[-1][0]: selected.append(unselected)

    return combine([i[1] for i in selected])
