class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        xor = 0
        h = {}
        count = 0
        for i in range(len(A)):
            xor ^= A[i]
            if xor == B:
                count += 1
            if xor^B in h:
                count += h[xor^B]
            if xor in h:
                h[xor] += 1
            else:
                h[xor] = 1
        return count
