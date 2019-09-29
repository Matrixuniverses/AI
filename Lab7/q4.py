from n_queens_neighbours import n_queens_neighbours as neighbours
from n_queens_neighbours import n_queens_cost as cost
from greedy_descent import *
import random

def main():
    # Test case 1
    print("\nTest case 1\n")

    N = 6
    random.seed(0)

    def random_state():
            return tuple(random.sample(range(1,N+1), N))   

    greedy_descent_with_random_restart(random_state, neighbours, cost)


    # Test case 2
    print("\nTest case 2\n")

    N = 8
    random.seed(0)

    def random_state():
        return tuple(random.sample(range(1,N+1), N))   

    greedy_descent_with_random_restart(random_state, neighbours, cost)


if __name__ == "__main__":
    main()

