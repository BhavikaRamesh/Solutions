class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rowLength = len(matrix)
        colLength = len(matrix[0])
        row = [0] * rowLength
        col = [0] * colLength
        for i in range(rowLength):
            for j in range(colLength):
                if matrix[i][j] == 0:
                    row[i] = 1
                    col[j] = 1
        for i in range(rowLength):
            for j in range(colLength):
                if row[i] or col[j]:
                    matrix[i][j] = 0
