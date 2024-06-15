class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                if (nums[i] + nums[j] + nums[k]) == 0:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif (nums[i] + nums[j] + nums[k]) > 0:
                    k -= 1
                else:
                    j += 1
        return s
