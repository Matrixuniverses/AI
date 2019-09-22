import math
import random
from n_queens_neighbours import n_queens_neighbours as neighbours
from n_queens_neighbours import n_queens_cost as cost

def greedy_descent(start_state, neighbours, cost):
    states_visited, current_state, select = [start_state], start_state, True
    yield current_state

    while select:
        select = False
        next_states = [(next_state, cost(next_state)) for next_state in neighbours(current_state)]

        if len(next_states) == 0: break

        next_state = min(next_states, key=lambda x: x[1])

        if cost(current_state) > next_state[1]:
            current_state = next_state[0]
            select = True

            yield current_state

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    g_min, l_min = 0, math.inf
    
    while l_min > g_min:
        states = list(greedy_descent(random_state(), neighbours, cost))
        l_min = min(cost(states) for states in states)

        print(*states, sep="\n")
        
        if l_min > g_min: print('RESTART', end="\n")


