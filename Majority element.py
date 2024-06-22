// Element occuring more than half the size of array
class Solution:
    def majorityElement(self, A, N):
        #Your code here
        d = {}
        for i in A:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        maxCount = max(d.values())
        key = 0
        for k, v in d.items():
            if v == maxCount:
                key = k
        if maxCount > int(N / 2):
            return key
        else:
            return -1
