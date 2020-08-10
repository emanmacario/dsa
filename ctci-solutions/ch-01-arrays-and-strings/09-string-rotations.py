# String Rotation: Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
# Hints: #34, #88, #104


def is_substring(string, substring):
    return substring in string


def string_rotation(s1, s2):
    """
    Runtime varies on runtime of is_substring
    Assuming is_substring is O(A + B), then
    this algorithm has O(N) time complexity
    """
    assert(len(s1) == len(s2) and s1 and s2)
    return is_substring(s1 + s1, s2)


if __name__ == "__main__":
    s1 = 'erbottlewat'
    s2 = 'waterbottle'
    print(string_rotation(s1, s2))

    s3 = 'macarioemmanuel'
    s4 = 'emmanuelmacario'
    print(string_rotation(s3, s4))

    s5 = 'hello joseph'
    s6 = 'joseph hello'
    print(string_rotation(s5, s6))

