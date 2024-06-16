class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        li = [0 for _ in range(numRows)]
        for i in range(numRows):
            li[i] = [0 for _ in range(i + 1)]
            li[i][i] = 1
            li[i][0] = 1
            for j in range(1, i):
                li[i][j] = li[i - 1][j] + li[i - 1][j - 1]
        return li
