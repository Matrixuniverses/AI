from itertools import product
from joint_prob import joint_prob

def query(network, query_var, evidence):
    hidden_vars = network.keys() - evidence.keys() - {query_var}
    pt, pf = 0, 0

    for values in product((True, False), repeat=len(hidden_vars)):
        hidden_assignments = {var: val for var, val in zip(hidden_vars, values)}

        pt += joint_prob(network, dict({query_var: True}, **evidence, **hidden_assignments))
        pf += joint_prob(network, dict({query_var: False}, **evidence, **hidden_assignments))

    return {True: pt / (pt + pf), False: pf / (pt + pf)}
