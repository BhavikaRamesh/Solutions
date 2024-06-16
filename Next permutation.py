class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length == 1:
            return nums
        for k in range(length - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                for l in range(length - 1, k, -1):
                    if nums[k] < nums[l]:
                        nums[l], nums[k] = nums[k], nums[l]
                        nums[k + 1:] = nums[k + 1:][::-1]
                        return nums
        nums.sort()
        return nums
