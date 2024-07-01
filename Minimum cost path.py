import sys

def helper(cost, x, y, i, j, dp):
    if i == x and j == y: return cost[i][j]
    if dp[i][j] != -1: return dp[i][j]
    # down
    down = sys.maxsize
    if i < x:
        down = cost[i][j] + helper(cost, x, y, i + 1, j, dp)
    # right
    right = sys.maxsize
    if j < y:
        right = cost[i][j] + helper(cost, x, y, i, j + 1, dp)
    # down right diagonal
    diagonal = sys.maxsize
    if i < x and j < y:
        diagonal = cost[i][j] + helper(cost, x, y, i + 1, j + 1, dp)
    dp[i][j] = min(right, min(down, diagonal))
    return dp[i][j]

def minCostPath(cost, n, m, x, y):
    # Write your code here.
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    return helper(cost, x - 1, y - 1, 0, 0, dp)
