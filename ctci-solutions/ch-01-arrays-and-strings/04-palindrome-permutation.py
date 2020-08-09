# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)
# Hints: #106, #121, #134, #136
import sys
from collections import Counter


def palindrome_permutation(string):
    """
    Solution is O(N) time complexity, O(N) space complexity
    :param string:
    :return:
    """
    # Remove whitespace chars
    stripped_string = string.lower().replace(' ', '')

    # Obtain character counts
    counts = Counter(stripped_string)
    evens = odds = 0
    for char, count in counts.items():
        if count % 2 == 0:
            evens += 1
        else:
            odds += 1

    # If there is an odd number (greater than one) of characters that
    # have odd frequencies, then cannot be a permutation of a palindrome
    if odds > 1 and odds % 2 == 1:
        return False
    return True


if __name__ == "__main__":
    string = sys.argv[-1]
    print(palindrome_permutation(string))
