def joint_prob(network, assignment):
    probability = 1

    for key in assignment.keys():
        truths = tuple([assignment[x] for x in network[key]['Parents']])
        probability *= network[key]['CPT'][truths] if assignment[key] else (1 - network[key]['CPT'][truths])

    return probability
