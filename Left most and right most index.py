class Solution:
    def indexes(self, v, x):
        d = {}
        if x not in v:
            return [-1, -1]
        ans = v.count(x)
        idx = v.index(x)
        return [idx, ans + idx - 1]
