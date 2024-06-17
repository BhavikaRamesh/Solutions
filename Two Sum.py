class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        for i in range(len(nums)):
            if (target - nums[i]) in d and d[target - nums[i]] != i:
                return [i, d[target - nums[i]]]
        return []


// Approach 2 from Interview Bit
class Solution:
	# @param A : tuple of integers
	# @param B : integer
	# @return a list of integers
	def twoSum(self, A, B):
        d = {}
        for i in range(len(A)):
            if B - A[i] in d:
                return [d[B - A[i]] + 1, i + 1]
            if A[i] not in d:
                d[A[i]] = i
        return []
