# TLE TC : O(2^N)
class Solution:
    def minInsertions(self, s: str) -> int:
        def insertions(s, i, j):
            if i >= j: return 0
            if s[i] == s[j]:
                return insertions(s, i + 1, j - 1)
            insertAtFront = 1 + insertions(s, i, j - 1)
            insertAtBack = 1 + insertions(s, i + 1, j)
            return min(insertAtFront, insertAtBack)
        start = 0
        end = len(s) - 1
        return insertions(s, start, end)

# TC : O(
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for gap in range(1, n):
            low = 0
            for high in range(gap, n):
                if s[low] == s[high]:
                    dp[low][high] = dp[low + 1][high - 1]
                else:
                    dp[low][high] = 1 + min(dp[low][high - 1], dp[low + 1][high])
                low += 1
        return dp[0][-1]
