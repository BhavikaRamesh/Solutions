class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        number = str(1 + int(''.join(str(x) for x in A) ))
        ret = [int(item) for item in number]
        return ret
