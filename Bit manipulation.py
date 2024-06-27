# Count set bits
def countSetBits(n):
	c = 0
	while n:
		n = n & n - 1
		c += 1
	return c

# Check kth bit is set or not
n, i = map(int, input().strip().split())
def solve(n, k):
	return "true" if (n & (1 << k)) != 0 else "false"
print(solve(n, i))


# Check if n is a power of 2
def solve(n):
	return (n & n - 1) == 0 and n != 0
for _ in range(int(input())):
	n = int(input())
	print(solve(n))

# No. of bits to flip to get B from A
def countSetBits(n):
	c = 0
	while n:
		n = n & n - 1
		c += 1
	return c

def solve(a, b):
	n = a ^ b
	ans = countSetBits(n)
	return ans
	
for _ in range(int(input())):
	a, b = map(int, input().strip().split())
	print(solve(a, b))


# Reverse bits
def reverseBits(n):
	a = '{:032b}'.format(n)[::-1]
	return int(a, 2)
t = int(input())
for i in range(t):
	n = int(input())
	print(reverseBits(n))

# Swap bits
def solve(n):
	mask_odd = 0x55555555
	mask_even = 0xAAAAAAAA
	odd_bits = n & mask_odd
	even_bits = n & mask_even
	shift_odd = odd_bits << 1
	shift_even = even_bits >> 1
	return shift_odd | shift_even
t = int(input())
for i in range(t):
	n = int(input())
	print(solve(n))

# 2 ^ K + 2 ^ N
n1, n2 = input().strip().split()
k, n = int(n1), int(n2)
print((1 << k) + (1 << n))

# Set kth bit to 1
def setBit(a, k):
	m = 1 << k
	return a | m
n1, n2 = input().strip().split()
a, k = int(n1), int(n2)
print(setBit(a, k))
