class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = [nums[0]] * n
        mini = [nums[0]] * n
        for i in range(1, n):
            maxi[i] = max(nums[i], maxi[i - 1] * nums[i], mini[i - 1] * nums[i])
            mini[i] = min(nums[i], maxi[i - 1] * nums[i], mini[i - 1] * nums[i])
        return max(maxi)
