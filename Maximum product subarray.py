class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = [nums[0]] * n
        mini = [nums[0]] * n
        for i in range(1, n):
            maxi[i] = max(nums[i], maxi[i - 1] * nums[i], mini[i - 1] * nums[i])
            mini[i] = min(nums[i], maxi[i - 1] * nums[i], mini[i - 1] * nums[i])
        return max(maxi)


class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		mini = arr[0]
		maxi = arr[0]
		curr = arr[0]
		for i in range(1, n):
		    if arr[i] < 0:
		        maxi, mini = mini, maxi
		    maxi = max(arr[i], arr[i] * maxi)
		    mini = min(arr[i], arr[i] * mini)
		    curr = max(curr, maxi)
		return curr
		
