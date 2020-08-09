# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# Hints:#23, #97, #130

def one_away(s1, s2):
    pass


if __name__ == "__main__":
    print(one_away('pale', 'ple'))
    print(one_away('pales', 'pale'))
    print(one_away('pale', 'bale'))
    print(one_away('pale', 'bake'))
