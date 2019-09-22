def roulette_wheel_select(population, fitness, r):
    total_fitness = sum(fitness(x) for x in population)
    n = total_fitness * r
    total = 0

    for p in population:
        total += fitness(p)
