class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = set()
        nums = sorted(nums)
        ans = nums[0] + nums[1] + nums[2]
        if ans > target:
            return ans
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while k > j:
                total = nums[i] + nums[j] + nums[k]
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    return total
                if (abs(target - total) < abs(target - ans)):
                    ans = total
        return ans
