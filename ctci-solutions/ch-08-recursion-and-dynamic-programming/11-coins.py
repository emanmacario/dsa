# Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), 
# nickels (5 cents), and pennies (1 cent), write code to calculate the number 
# of ways of representing n cents.
# Hints: #300, #324, #343, #380, #394


# -- Solution

def make_change(n, coins=[1, 5, 10, 25]):
    """
    Uses DP to compute the total number of unique ways of representing
    n cents, using an infinite number of a set of coins

    Solution is O(n) space and O(nk) time (where k is number of coins).
    In the case using the standard American coins, the solution is O(n).

    Space complexity has been optimised from O(nk) to O(n) by recognising
    that after filling the 'j'th row we do not need the 'j-1'th row. 
    Hence, we continuously overwrite one row during the loop
    """
    k = len(coins)

    dp = [1] + [0] * n
    for i in range(1, k + 1):
        coin = coins[i-1]
        for j in range(1, n + 1):
            dp[j] = dp[j] + (dp[j-coin] if j - coin >= 0 else 0)

    return dp[n]

    
# -- Testing

if __name__ == '__main__':
    print(make_change(5, coins=[1, 2, 5]))