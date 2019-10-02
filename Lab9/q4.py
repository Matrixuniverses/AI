from learn_likelihood import learn_likelihood

def main():

    # Test case 1
    print("\nTest case 1\n")

    likelihood = learn_likelihood("spam-labelled.csv")
    print(len(likelihood))
    print([len(item) for item in likelihood])


    # Test case 2
    print("\nTest case 2\n")

    likelihood = learn_likelihood("spam-labelled.csv")

    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

    # Test case 3
    print("\nTest case 3\n")

    likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)

    print("With Laplacian smoothing:")
    print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
    print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
    print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
    print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))

if __name__ == "__main__":
    main()
