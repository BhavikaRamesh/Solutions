# def transposeMatrix(a, n):
# 	for i in range(n):
# 		for j in range(i, n):
# 			a[i][j], a[j][i] = a[j][i], a[i][j]
# 	return a
	
# def reverseMatrix(li, n):
# 	li = transposeMatrix(li, n)
# 	for i in range(n):
# 		left, right = 0, n - 1
# 		while left < right:
# 			li[i][left], li[i][right] = li[i][right], li[i][left]
# 			left += 1
# 			right -= 1
# 	return li
def sumOfOneDiagonal(li, i, j):
	s = 0
	n = len(li)
	while i < n and j < n:
		s += li[i][j]
		i += 1
		j += 1
	print(s, end = ' ')
	
def sumOfAllDiagonals(li, n):
	for i in range(n - 1, -1, -1):
		sumOfOneDiagonal(li, 0, i)
	for i in range(1, n):
		sumOfOneDiagonal(li, i, 0)


for i in range(int(input())):
	n = int(input())
	li = []
	for _ in range(n):
		r = list(map(int, input().strip().split()))
		li.append(r)
	sumOfAllDiagonals(li, n)
	print()
	
