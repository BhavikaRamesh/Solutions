// Element occuring more than half the size of array
import math
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        maxOccurence = math.floor(len(A) / 2)
        for k, v in d.items():
            if v > maxOccurence:
                return k
                
