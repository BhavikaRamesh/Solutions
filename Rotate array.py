class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(startIdx, finishIdx):
            while startIdx < finishIdx:
                nums[startIdx], nums[finishIdx] = nums[finishIdx], nums[startIdx]
                startIdx += 1
                finishIdx -= 1
        
        k %= len(nums)
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
