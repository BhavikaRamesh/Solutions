#Hint
#         Sum(Actual) = Sum(1...N) + A - B

#     Sum(Actual) - Sum(1...N) = A - B. 

#     Sum(Actual Squares) = Sum(1^2 ... N^2) + A^2 - B^2

#     Sum(Actual Squares) - Sum(1^2 ... N^2) = (A - B)(A + B) 

#     = (Sum(Actual) - Sum(1...N)) ( A + B). 
# We can use the above 2 equations to get the value of A and B.

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        sumN = (n * (n + 1)) // 2
        sumN2 = (n * (n + 1) * (2 * n + 1)) // 6
        actualN = sum(A)
        actualN2 = sum(x ** 2 for x in A)
        diffN = actualN - sumN
        diffN2 = actualN2 - sumN2
        a = (diffN + diffN2 // diffN) // 2
        b = a - diffN
        return [a, b]
        
        
