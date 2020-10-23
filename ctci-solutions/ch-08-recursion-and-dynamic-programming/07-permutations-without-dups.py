# Permutations without Dups: Write a method to compute all permutations of a 
# string of unique characters.
# Hints: #150, #185, #200, #267, #278, #309, #335, #356


# -- Solution

"""
Example:
    Input string is CAT

    Base Case: [T]
    2 Character case: [AT, TA]
    3 Character case: [CAT, ACT, ATC, CTA, TCA, TAC]
"""

def permutations(s):
    """
    Computes all permutations of a string of unique characters
    Time and space complexity is O(N.N!), since there are N!
    possible permutations each of length N. (Not sure if I am correct w.r.t
    algorithmic complexity here)
    """
    # Base case: a single char
    if len(s) == 1:
        return [s]

    # Recursive case: intersperse first char between all permutations of the next n-1 chars
    result = []
    c = s[0]
    for sequence in permutations(s[1:]):
        for i in range(len(sequence) + 1):
            permutation = f"{sequence[:i]}{c}{sequence[i:]}"
            result.append(permutation)
    
    return result


# -- Testing

if __name__ == '__main__':
    p = permutations('cat')
    print(p)