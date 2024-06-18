class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        r, c = len(matrix), len(matrix[0])
        high = r * c - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            row, col = mid // c, mid % c
            element = matrix[row][col]
            if element == target:
                return True
            elif element > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
