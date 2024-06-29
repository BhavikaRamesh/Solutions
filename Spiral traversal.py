def spiral(li, n):
    l, r, t, b = 0, n - 1, 0, n - 1
    # 0 -> L to R, 1 -> T to B, 2 -> R to L, 3 -> B to T
    dir = 0
    while l <= r and t <= b:
    	if dir == 0:
    		for i in range(l, r + 1):
    			print(li[t][i], end = ' ')
    		t += 1
    	if dir == 1:
    		for i in range(t, b + 1):
    			print(li[i][r], end = ' ')
    		r -= 1
    	if dir == 2:
    		for i in range(r, l - 1, -1):
    			print(li[b][i], end = ' ')
    		b -= 1
    	if dir == 3:
    		for i in range(b, t - 1, -1):
    			print(li[i][l], end = ' ')
    		l += 1
    	dir = (dir + 1) % 4
    			
for _ in range(int(input())):
	n = int(input())
	li = []
	for _ in range(n):
		li.append(list(map(int, input().strip().split())))
	spiral(li, n)
	print()
