# Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with 
# r rows and c columns. The robot can only move in two directions, right and 
# down, but certain cells are "off limits" such that the robot cannot step on 
# them. Design an algorithm to find a path for the robot from the top left to
# the bottom right.
# Hints: #331, #360, #388


# -- Solution to unique paths without obstacles

def unique_paths_dp(m, n):
    dp = [[1 for _ in range(n)] for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


def print_dp(dp):
    """
    Helper function to print DP matrix
    """
    for row in dp:
        print(''.join(f'{n:3} ' for n in row))


# -- Solution to unique paths with obstacles

def uniquePathsWithObstacles(obstacleGrid):
    """
    Both time and space complexity are O(MN), where M and N are
    dimensions of the grid.
    """
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]

    # Initialise base case values in top row and leftmost column,
    # placing zero values for grid cells that we cannot reach
    row = col = 0
    while col < n and obstacleGrid[0][col] != 1:
        dp[0][col] = 1
        col += 1
        
    while row < m and obstacleGrid[row][0] != 1:
        dp[row][0] = 1
        row += 1
    
    # Compute total number of unique paths
    for y in range(1, m):
        for x in range(1, n):
            if obstacleGrid[y][x] == 1:
                continue
            dp[y][x] = ((dp[y-1][x] if obstacleGrid[y-1][x] != 1 else 0) + 
                        (dp[y][x-1] if obstacleGrid[y][x-1] != 1 else 0))

    return dp[m-1][n-1] if obstacleGrid[m-1][n-1] != 1 else 0


if __name__ == '__main__':
    obstacleGrid = [
        [0,0,0,0],
        [0,1,0,0],
        [0,1,0,0]
    ]
    print(uniquePathsWithObstacles(obstacleGrid))  # 3