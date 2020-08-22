# Permutations without Dups: Write a method to compute all permutations of a 
# string of unique characters.
# Hints: #150, #185, #200, #267, #278, #309, #335, #356


# -- Solution

def permutations(s):
    """
    Computes all permutations of a string of unique characters
    Time and space complexity is O(N.N!), since there are N!
    possible permutations each of length N. (Not sure if I am correct w.r.t
    algorithmic complexity here)
    """
    if len(s) == 1:
        return [s]

    result = []
    c = s[0]
    for sequence in permutations(s[1:]):
        for i in range(len(sequence) + 1):
            result.append(sequence[:i] + c + sequence[i:])
    
    return result


# -- Testing

if __name__ == '__main__':
    p = permutations('cat')
    print(set(p))
    print(p)