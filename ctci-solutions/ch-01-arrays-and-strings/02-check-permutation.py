# Given two strings, write a method to decide if one is a permutation of the
# other
from collections import Counter


def check_permutation(s1, s2):
    return Counter(s1) == Counter(s2)


def main():
    s1 = 'emmanuel'
    s2 = 'manuelme'
    print(check_permutation(s1, s2))

    s3 = 'racecar'
    s4 = 'racecar'
    print(check_permutation(s3, s4))


if __name__ == "__main__":
    main()
