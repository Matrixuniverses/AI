from posterior import posterior

def nb_classify(prior, likelihood, input_vector):
    spam_prob = posterior(prior, likelihood, input_vector)
    return ("Spam", spam_prob) if spam_prob > 0.5 else ("Not Spam", (1 - spam_prob))
