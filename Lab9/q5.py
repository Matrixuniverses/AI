from learn_prior import learn_prior
from learn_likelihood import learn_likelihood
from nb_classify import nb_classify

def main():
    # Test case 1
    print("\nTest case 1\n")

    prior = learn_prior("spam-labelled.csv")
    likelihood = learn_likelihood("spam-labelled.csv")

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))

    # Test case 2
    print("\nTest case 2\n")

    prior = learn_prior("spam-labelled.csv", pseudo_count=1)
    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    input_vectors = [
        (1,1,0,0,1,1,0,0,0,0,0,0),
        (0,0,1,1,0,0,1,1,1,0,0,1),
        (1,1,1,1,1,0,1,0,0,0,1,1),
        (1,1,1,1,1,0,1,0,0,1,0,1),
        (0,1,0,0,0,0,1,0,1,0,0,0),
        ]

    predictions = [nb_classify(prior, likelihood, vector) 
                   for vector in input_vectors]

    for label, certainty in predictions:
        print("Prediction: {}, Certainty: {:.5f}"
              .format(label, certainty))


if __name__ == "__main__":
    main()
