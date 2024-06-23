class Solution:	
	def remove_duplicate(self, A, N):
		i = 0
        for j in range(1, N):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        return i + 1
