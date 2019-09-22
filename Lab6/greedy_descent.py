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
    print("ligma")

