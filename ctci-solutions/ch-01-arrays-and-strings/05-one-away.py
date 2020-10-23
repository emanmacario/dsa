# One Away: There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.
# EXAMPLE
# pale, ple -> true
# pales, pale -> true
# pale, bale -> true
# pale, bake -> false
# Hints:#23, #97, #130


def one_edit_away(first, second):
    if len(first) == len(second):
        return one_edit_replace(first, second)
    elif len(first) + 1 == len(second):
        return one_edit_insert(first, second)
    elif len(first) - 1 == len(second):
        return one_edit_insert(second, first)

    return False


# -- Helper Functions
def one_edit_replace(first, second):
    """
    Checks if same length strings differ in at most one position
    """
    diffs = 0
    for c1, c2 in zip(first, second):
        if c1 != c2:
            diffs += 1
            if diffs > 1:
                return False
    return True


def one_edit_insert(first, second):
    """
    Checks if you can insert a character into first to make it second
    Note that first is shorter than second by one char 
    """
    # Solution is O(N) where N is length of shorter string
    i = j = 0
    while i < len(first) and j < len(second):
        # First, check if chars are the same at the indexes
        if first[i] == second[j]:
            # If so, increment pointers
            i += 1
            j += 1
        else:
            # If the pointers do not match, and the check above has failed,
            # then we can return false
            if i != j:
                return False

            # j should only ever be incremented in isolation once
            j += 1

    return True


if __name__ == "__main__":
    print(one_edit_away('pale', 'ple'))
    print(one_edit_away('pales', 'pale'))
    print(one_edit_away('pale', 'bale'))
    print(one_edit_away('pale', 'bake'))

