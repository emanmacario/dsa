# Write a program that takes as input a set of sorted sequences and computes the 
# union of these sequences as a sorted sequence. For example, if the input is 
# <3,5,7>, <0,5>, and <0,6,28>, then the output is <0,0,3,5,6,6,7,28>


# -- Solution

import heapq

def merge_sorted_arrays(arrays):
    """
    This is a Pythonic solution that uses a min-heap of 
    size K, where K is total number of sequences, to
    incrementally build a sorted merge array
    """
    return list(heapq.merge(*arrays))
    

def merge_sorted_arrays_prime(arrays):
    """
    A rudimentary solution using the same concepts
    """
    pass



# -- Testing

from pprint import pprint

if __name__ == '__main__':
    sequences = [
        [3, 5, 7],
        [0, 5],
        [0, 6, 28]
    ]
    pprint(sequences)
    print(merge_sorted_arrays(sequences))