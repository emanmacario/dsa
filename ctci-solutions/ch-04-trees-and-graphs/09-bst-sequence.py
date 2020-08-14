# BST Sequences: A binary search tree was created by traversing through an array 
# from left to right and inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could have led to this tree.
# EXAMPLE
# Input:
#     2
#    / \
#   1   3
# Output: {2, 1, 3}, {2, 3, 1}
# Hints: #39, #48, #66, #82


# -- Solution

from binary_search_tree import TreeNode


def all_sequences(node):
    """
    Generates all possible arrays of values that when inserted
    into a BST, generates the exact tree with root 'node'
    """
    result = []

    if not node:
        result.append([])
        return result

    prefix = [node.val]

    # Recurse on left and right subtrees
    left_sequences = all_sequences(node.left)
    right_sequences = all_sequences(node.right)

    # Weave together lists from left and right sides
    for left in left_sequences:
        for right in right_sequences:
            weaved = []
            weave_lists(left, right, weaved, prefix)
            print(weaved)
            result.extend(weaved)

    return result


def weave_lists(first, second, results, prefix):
    """
    Weaves lists together in all possible ways. This algorithm
    works be removing the head from one list, recursing, and then
    doing the same thing with the other list
    """
    # One list is empty, add remainder to prefix and store result
    if not first or not second:
        return results.append(prefix + first + second)

    # Recurse with head of first added to the prefix
    first_head, first_tail = first[0], first[1:]
    weave_lists(first_tail, second, results, prefix + [first_head])

    # Do the same thing with second
    second_head, second_tail = second[0], second[1:]
    weave_lists(first, second_tail, results, prefix + [second_head])



# -- Testing

from random import randint, seed


def is_equal(T1, T2):
    """
    Checks if two trees are equal with respect to structure and values
    """
    # Both empty
    if not T1 and not T2:
        return True

    # One empty
    if not T1 or not T2:
        return False

    # Non-equal values
    if T1.val != T2.val:
        return False

    # Otherwise, check that subtrees are equivalent
    return is_equal(T1.left, T2.left) and is_equal(T1.right, T2.right)


def check_sequences(tree, sequences):
    """
    Creates a tree for each sequence in sequence and
    checks if it is equal to the original tree that
    generated all the sequences
    """
    for sequence in sequences:
        root, *rest = sequence
        sequence_tree = TreeNode(root)
        for val in rest:
            sequence_tree.insert(val)

        if not is_equal(tree, sequence_tree):
            print(sequence)
            sequence_tree.display()
            return False
    
    return True


if __name__ == "__main__":
    tree = TreeNode(randint(0, 100))
    for _ in range(6):
        tree.insert(randint(0, randint(0, 100)))

    print('--- Original Tree ---')
    tree.display()
    
    print('\n--- Weaved ---')
    sequences = all_sequences(tree)

    print('\n--- BST Sequences ---')
    for sequence in sequences:
        print(sequence)

    print('\n--- Checking Equality Between Sequences ---')
    if check_sequences(tree, sequences):
        print('All OK')
    else:
        print('Not all OK')