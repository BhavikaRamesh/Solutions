class Solution:
    def convertToWave(self, n : int, arr : List[int]) -> None:
        evenIdx = []
        for i in range(1, n, 2):
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
