class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maximumArea = 0
        while (left < right):
            # Taking lesser height cause if bigger height is taken, then water might overflow
            # Area = width * height
            currentArea = min(height[left], height[right]) * (right - left)
            maximumArea = max(maximumArea, currentArea)
            if height[left] < height[right]: left += 1
            elif height[left] > height[right]: right -= 1
            else: 
                left += 1
                right -= 1
        return maximumArea
