from posterior import posterior


def main():
    # Test case 1
    print("\nTest case 1\n")

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (True, True, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true)) 

    # Test case 2
    print("\nTest case 2\n")

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (True, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  


    # Test case 3
    print("\nTest case 3\n")


    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (False, False, True)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))  

    # Test case 4
    print("\nTest case 4\n")

    prior = 0.05
    likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

    observation = (False, False, False)

    class_posterior_true = posterior(prior, likelihood, observation)
    print("P(C=False|observation) is approximately {:.5f}"
          .format(1 - class_posterior_true))
    print("P(C=True |observation) is approximately {:.5f}"
          .format(class_posterior_true))


if __name__ == "__main__":
    main()
