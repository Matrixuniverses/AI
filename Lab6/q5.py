from roulette_wheel_select import roulette_wheel_select

def main():
    # Test case 1
    print("\nTest case 1\n")

    population = ['a', 'b']

    def fitness(x):
        return 1 # everyone has the same fitness

    for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
        print(roulette_wheel_select(population, fitness, r))

    # Test case 2
    print("\nTest case 2\n")

    population = [0, 1, 2]

    def fitness(x):
        return x

    for r in [0, 0.33, 0.34, 0.5, 0.75, 0.99]:
        print(roulette_wheel_select(population, fitness, r))

if __name__ == "__main__":
    main()
