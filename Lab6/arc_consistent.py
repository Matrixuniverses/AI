import itertools, copy
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    tda = {(x, c) for c in csp.constraints for x in csp.var_domains}
    while tda:
        x, c = tda.pop()
        ys = list(scope(c) - {x})
        new_domain = set()
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            csp.var_domains[x] = new_domain
            for cprime in set(csp.constraints) - {c}:
                if x in scope(c):
                   for z in scope(cprime):
                       if x != z:
                           tda.add((z, cprime))
    return csp