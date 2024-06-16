class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_now = nums[0]
        cur_max = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_now = max(max_now, cur_max)
        return max_now
