# Parens: Implement an algorithm to print all valid (i.e. properly opened and 
# closed) combinations of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
# Hints: #138, #174, #187, #209, #243, #265, #295


# -- Solution

def parens_prime(N):
    """
    Generates all valid combinations of n parentheses. Builds the 
    string from scratch. Under this approach, we add left and right 
    parens, as long as the expression stays valid. I think time
    complexity is O(2^N), while space complexity is O(N).
    """

    def add_paren(result, left_rem, right_rem, string, index):
        """
        Recursive helper function that adds a single parentheses
        and recurses, adding valid combinations to the result list
        """
        # Invalid state
        if left_rem < 0 or right_rem < left_rem:
            return

        # Out of left and right parentheses
        if left_rem == 0 and right_rem == 0:
            result.append(''.join(string))
        else:
            # Add left and recurse
            string[index] = '('
            add_paren(result, left_rem - 1, right_rem, string, index + 1)

            # Add right and recurse
            string[index] = ')'
            add_paren(result, left_rem, right_rem - 1, string, index + 1)

    # Generate and return valid combinations
    result = []
    add_paren(result, N, N, [''] * N * 2, 0)
    return result


    
# -- Testing

from pprint import pprint

if __name__ == '__main__':
    pprint(sorted(parens(4)))
