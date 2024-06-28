class Solution:
    def lcmAndGcd(self, A , B):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        gcdv = gcd(A, B)
        lcm = (A * B) // gcdv
        return [lcm, gcdv]
