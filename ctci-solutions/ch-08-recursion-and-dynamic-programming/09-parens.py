# Parens: Implement an algorithm to print all valid (i.e. properly opened and 
# closed) combinations of n pairs of parentheses.
# EXAMPLE
# Input: 3
# Output: ( ( () ) ) , ( () () ) , ( () ) () , () ( () ) , () () ()
# Hints: #138, #174, #187, #209, #243, #265, #295


# -- Solutions

# -- Solution One: Naive algorithm, which generates duplicates

def parens(N):
    """
    Prints all valid combinations of n pairs of parentheses.
    Algorithm generates duplicates, hence the type conversion
    in the return statement
    """
    # Base case
    if N == 1:
        return ['()']

    # Recursive case
    base, result = parens(N-1), []
    for combination in base:
        new_combinations = [
            combination + '()',
            '()' + combination,
            '(' + combination + ')'
        ]
        result.extend(new_combinations)

    return set(result)
    

# -- Solution Two: Smarter algorithm, avoids duplicates

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

if __name__ == '__main__':
    # combinations = parens(5)
    # for c in combinations:
    #     print(c)

    print(parens_prime(3))