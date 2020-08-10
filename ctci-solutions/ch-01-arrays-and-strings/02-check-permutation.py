# Given two strings, write a method to decide if one is a permutation of the
# other
from collections import Counter


def check_permutation(s1, s2):
    # Solution: O(N) space and time complexity
    return Counter(s1) == Counter(s2)


"""
Counter comparison time analysis explanation (from Stack Overflow):
- There is an early exit if the number of keys is different (this does not influence big-O).
- Then a loop that iterates over all the keys that exits early if the key is not found, or if the corresponding value is 
different (again, this has no bearing on big-O)
- If all keys are found, and the corresponding values are all equal, then the dictionaries are declared equal
- The lookup and comparisons of each key-value pair is O(1); this operation is repeated at most N times (N being the 
number of keys) 
- In all, the time complexity is O(N), with N the number of keys
"""



def main():
    s1 = 'emmanuel'
    s2 = 'manuelme'
    print(check_permutation(s1, s2))

    s3 = 'racecar'
    s4 = 'racecar'
    print(check_permutation(s3, s4))


if __name__ == "__main__":
    main()
