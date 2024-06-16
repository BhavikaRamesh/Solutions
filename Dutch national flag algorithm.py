class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # zero = nums.count(0)
        # one = nums.count(1)
        # for i in range(zero):
        #     nums[i] = 0
        # for i in range(zero, zero + one):
        #     nums[i] = 1
        # for i in range(one + zero, len(nums)):
        #     nums[i] = 2
        i = 0
        j = len(nums) - 1
        mid = 0
        while mid <= j:
            if nums[mid] == 0:
                nums[i], nums[mid] = nums[mid], nums[i]
                i += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[j] = nums[j], nums[mid]
                j -= 1
