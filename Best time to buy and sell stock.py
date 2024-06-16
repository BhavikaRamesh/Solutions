class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in prices:
            minPrice = min(i, minPrice)
            maxProfit = max(maxProfit, abs(i - minPrice))
        return maxProfit
