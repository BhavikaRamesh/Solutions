class Solution:
    def minDistanceHelper(self, word1, word2, i, j):
        m, n = len(word1), len(word2)
        dp = [[-1 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    ins = dp[i][j - 1]
                    dele = dp[i - 1][j]
                    rep = dp[i - 1][j - 1]
                    dp[i][j] = min(ins, min(dele, rep)) + 1
        return dp[m][n]
    
    def minDistance(self, word1: str, word2: str) -> int:
        return self.minDistanceHelper(word1, word2, len(word1), len(word2))
