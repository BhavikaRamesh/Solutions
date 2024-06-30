class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []

        def flip(k):
            l, r = 0, k-1
            while l < r:
                arr[l], arr[r] = arr[r], arr[l]
                l, r = l+1, r-1

        def findLargestIdx(n: int) -> int:
            maxi = arr[0]
            index = 0
            for i in range(n):
                if arr[i] > maxi:
                    maxi = arr[i]
                    index = i
            return index    
        
        n = len(arr)
        for i in range(n, 0, -1):
            maxIdx = findLargestIdx(i)
            if maxIdx != i - 1:
                if maxIdx != 0:
                    flip(maxIdx + 1)
                    result.append(maxIdx + 1)
                flip(i)
                result.append(i)
        return result
