class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 = nums1 + nums2
        nums1.sort()
        if len(nums1) % 2 == 1:
            middle = math.trunc(len(nums1) / 2)
            return nums1[middle]
        else:
            second = math.trunc(len(nums1) / 2)
            first = math.trunc(len(nums1) / 2) - 1
            return (nums1[first] + nums1[second]) / 2
