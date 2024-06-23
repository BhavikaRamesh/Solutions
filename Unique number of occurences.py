from typing import List


class Solution:
    def isFrequencyUnique(self, n : int, arr : List[int]) -> bool:
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        frequencies = d.values()
        if len(frequencies) == len(set(frequencies)):
            return True
        return False
        
