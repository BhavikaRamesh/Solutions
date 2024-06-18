class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        A = obstacleGrid
        m = len(A)
        n = len(A[0])
        dp = [[0 for c in range(n)] for r in range(m)]
        if A[0][0] == 0:
            dp[0][0] = 1
        for i in range(1, m):
            if A[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            if A[0][j] == 0:
                dp[0][j] = dp[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if A[i][j] != 1:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 
        return dp[m - 1][n - 1]
