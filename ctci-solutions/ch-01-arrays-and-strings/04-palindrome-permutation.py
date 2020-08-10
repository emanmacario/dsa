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
    """
    # Remove whitespace chars, O(N)
    stripped_string = string.lower().replace(' ', '')

    # Obtain character counts, O(N)
    counts = Counter(stripped_string)

    # Calculate number of odd occurring characters, O(N)
    odds = 0
    for char, count in counts.items():
        if count % 2 == 1:
            odds += 1

    # If there is an more than one character that has an odd frequency,
    # then cannot be a permutation of a palindrome, O(1)
    if odds > 1:
        return False
    return True


if __name__ == "__main__":
    """
    -- EXAMPLES
    Example 1:
        Input: "code"
        Output: False
    Example 2:
        Input: "aab"
        Output: True
    Example 3:
        Input: "carerac"
        Output: True
    """
    string = sys.argv[-1]
    print(palindrome_permutation(string))
