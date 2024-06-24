class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def solve(ind, target):
            if target == 0:
                return True
            if ind == 0:
                return nums[ind] == target
            if dp[ind][target] != -1:
                return dp[ind][target]
            notPick = solve(ind - 1, target)
            pick = False
            if nums[ind] <= target:
                pick = solve(ind - 1, target - nums[ind])
            dp[ind][target] = pick or notPick
            return dp[ind][target]


        s = sum(nums)
        n = len(nums)
        if s % 2 != 0:
            return False
        s //= 2
        dp = [[-1 for j in range(s + 1)] for i in range(n)]
        return solve(n - 1, s)
