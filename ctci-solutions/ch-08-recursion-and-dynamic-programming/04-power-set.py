# Power Set: Write a method to return all subsets of a set.
# Hints: #273, #290, #338, #354, #373


# -- Solution

def power_set(s):
    """
    Generates and returns the powerset (i.e. all subsets) of an input set.
    Both space and time complexity are O(n 2^n). This is because there are
    2^n subsets and each of the n elements appears in 2^n-1 subsets.
    """
    # Base case: empty set
    if not s:
        return [[]]
    
    # Recursive case: remove an element from the input set of size n, then generate
    # the powerset of the reduced mutated set of size n - 1. Next, copy each subset 
    # in the powerset and append the removed element to each copied subset
    element = s.pop()
    extension = []
    all_subsets = power_set(s)

    for subset in all_subsets:
        new_subset = list(subset)
        new_subset.append(element)
        extension.append(new_subset)

    all_subsets.extend(extension)

    return all_subsets

    
# -- Testing

from pprint import pprint

if __name__ == '__main__':
    ps = power_set([0, 1, 2])
    pprint(ps)
