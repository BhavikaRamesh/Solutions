class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        n = len(nums)
        nums.sort()
        for a in range(n):
            for b in range(a+1, n):
                c = b+1
                d = n-1
                while c<d:
                    sums = nums[a]+nums[b]+nums[c]+nums[d]
                    if sums < target:
                        c += 1
                    elif sums > target:
                        d -= 1
                    else:
                        total = [nums[a],nums[b],nums[c],nums[d]]
                        if total not in res:
                            res.append(total)
                        c +=1
                        d-=1
        return res
