from distances import *

def main():
    # Test case 1
    print("\nTest case 1\n")
    
    print(euclidean_distance([0, 3, 1, -3, 4.5],[-2.1, 1, 8, 1, 1]))

    # Test case 2
    print("\nTest case 2\n")

    print(majority_element([0, 0, 0, 0, 0, 1, 1, 1]))
    print(majority_element("abcabcabcabc") in "abc")

if __name__ == "__main__":
    main()
