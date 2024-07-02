from heapq import heapify, heappop, heappush
class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        heapify(arr)
        total = 0
        while len(arr) > 1:
            first = heappop(arr)
            second = heappop(arr)
            total += first + second
            heappush(arr, first + second)
        return total
        
