import sys
def maxProfit(values, weights, n, w):
    dp = [[0 for j in range(w + 1)] for i in range(n)]
    for i in range(weights[0], w + 1):
        dp[0][i] = values[0]
    for i in range(1, n):
        for j in range(w + 1):
            notTake = 0 + dp[i - 1][j]
            take = -sys.maxsize
            if weights[i] <= j:
                take = values[i] + dp[i - 1][j - weights[i]]
            dp[i][j] = max(take, notTake)
    return dp[n - 1][w]

