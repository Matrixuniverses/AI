def posterior(prior, likelihood, observation):
    pt, pf = prior, (1 - prior)
    
    for prob, obs in zip(likelihood, observation):
        pt *= prob[True] if obs else (1 - prob[True])
        pf *= prob[False] if obs else (1 - prob[False])

    return pt / (pt + pf)
