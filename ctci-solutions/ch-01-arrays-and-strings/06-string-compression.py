# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, #110
import sys


def string_compression(string):
    # Assume string is non-empty
    assert(string)

    orig_len, curr_len = len(string), 1
    output_string = ''
    for i in range(1, orig_len):
        prev, curr = string[i - 1], string[i]
        if curr != prev:
            output_string += f'{prev}{curr_len}'
            curr_len = 1
        else:
            curr_len += 1

    output_string += f'{curr}{curr_len}'
    output_len = len(output_string)

    return output_string if output_len < orig_len else string


if __name__ == "__main__":
    string = sys.argv[-1]
    print(string_compression(string))


