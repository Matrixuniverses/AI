from itertools import combinations

def n_queens_neighbours(state):
    neighbours = []
    
    for i, j in combinations(range(len(state)), 2):
        neighbour = list(state)
        neighbour[i], neighbour[j] = state[j], state[i]
        neighbours.append(tuple(neighbour))

    return sorted(neighbours)

def n_queens_cost(state):
    return len([s for s in combinations(enumerate(state), 2) if abs(s[0][0] - s[1][0]) == abs(s[0][1] - s[1][1])])
