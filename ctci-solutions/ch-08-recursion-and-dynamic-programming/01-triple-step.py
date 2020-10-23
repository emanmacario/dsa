# Triple Step: A child is running up a staircase with n steps and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many 
# possible ways the child can run up the stairs.
# Hints: #152, #178, #217, #237, #262, #359


# -- Solution

# Here is a general solution for climbing n steps with advance limit of k steps

def number_of_ways_to_top(top, maximum_step):
    """
    Solution has O(n) time complexity, and O(n) space complexity
    We use the formula given below to understand the problem:

        F(n, k) = sum F(n - i, k) for i = 1,..,k
        
        where F(0) = 1

    Where
        n: total number of steps to climb
        k: maximum number of steps to advance at a time (i.e. step-size in [1, k])
    """
    def compute_number_of_ways_to_h(h):
        # Differs from Fibonacci in sense that base case F(0) = 1, not 0
        if h <= 1:
            return 1
        
        if number_of_ways_to_h[h] == 0:
            number_of_ways_to_h[h] = sum(
                compute_number_of_ways_to_h(h - i) 
                for i in range(1, maximum_step + 1) if h - i >= 0)

        return number_of_ways_to_h[h]
    
    number_of_ways_to_h = [0] * (top + 1)
    return compute_number_of_ways_to_h(top)


# Here is a specific solution for k = 3 (not using general solution as a subroutine)

def triple_step(n):
    """
    Computes the total number of ways to climb a total of n 
    steps, climbing only 1, 2, or 3 steps at a time

    Solution has O(n) time complexity, and O(n) space complexity.
    Could make it O(1) space complexity if we choose to use three
    variables instead of an array of size O(n)
    """
    if n <= 1:
        return 1
    
    dp = [1, 1] + [0] * (n - 1)
    for i in range (2, n + 1):
        dp[i] = sum(dp[k] for k in range(i - 3, i) if k >= 0)

    return dp[n]


# -- Testing

if __name__ == "__main__":
    for top in range(1, 50):
        general = number_of_ways_to_top(top, 3)
        specific = triple_step(top)
        print(f'{general:10} {specific:10} {general == specific}')
