# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, #110
import sys


def string_compression(string):
    length = len(string)


if __name__ == "__main__":
    string = sys.argv[-1]
    print(string_compression(string))


