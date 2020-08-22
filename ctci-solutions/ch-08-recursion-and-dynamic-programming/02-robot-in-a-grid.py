# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with 
# r rows and c columns. The robot can only move in two directions, right and 
# down, but certain cells are "off limits" such that the robot cannot step on 
# them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
# Hints: #331, #360, #388


def unique_paths_dp(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def print_dp(dp):
    for row in dp:
        print(''.join(f'{n:3} ' for n in row))


if __name__ == '__main__':
    print(unique_paths_dp(7, 4))
