# Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

# Hint #53: It's often easiest to modify strings by going from the end of the string to the beginning.
# Hint #118: You might find you need to know the number of spaces. Can you just count them?
import sys


def urlify(string):
    return string.strip().replace(' ', '%20')


if __name__ == "__main__":
    # E.g. string "Mr John Smith" has 'true' length of 13
    string = sys.argv[-1]
    print(len(string))
    print(urlify(string))
