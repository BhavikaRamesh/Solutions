# TC : O(N), SC : O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lm, rm = height[l], height[r]
        water = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, height[l])
                water += lm - height[l]
            else:
                r -= 1
                rm = max(rm, height[r])
                water += rm - height[r]
        return water

# TC : O(N), SC : O(N)
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * n
        right = [0] * n
        water = 0
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        for i in range(n):
            water += min(left[i], right[i]) - height[i]
        return water


# TC : O(N^2), SC : O(N)
class Solution:
    def trappingWater(self, arr,n):
        #Code here
        res = 0
        for i in range(1, n - 1):
            left = arr[i]
            for j in range(i):
                left = max(left, arr[j])
            right = arr[i]
            for j in range(i + 1, n):
                right = max(right, arr[j])
            res = res + min(left, right) - arr[i]
        return res
