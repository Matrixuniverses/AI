from learn_prior import learn_prior

def main():
    # Test case 1
    print("\nTest case 1\n")

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of spam is {:.5f}.".format(prior))

    # Test case 2
    print("\nTest case 2\n")

    prior = learn_prior("spam-labelled.csv")
    print("Prior probability of not spam is {:.5f}.".format(1 - prior))

    # Test case 3
    print("\nTest case 3\n")

    prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
    print(format(prior, ".5f"))

    # Test case 4
    print("\nTest case 4\n")

    prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
    print(format(prior, ".5f"))

    # Test case 5
    print("\nTest case 5\n")

    prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
    print(format(prior, ".5f"))

    # Test case 6
    print("\nTest case 6\n")

    prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
    print(format(prior, ".5f"))


if __name__ == "__main__":
    main()
