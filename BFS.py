def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        visited = [False] * V
    	ans = []
    	q = deque()
    	q.append(0) # start vertex
    	visited[0] = True
    	while q:
    		v = q.popleft()
    		ans.append(v)
    		if len(adj[v]) > 0:
    			for i in adj[v]:
    				if not visited[i]:
    					q.append(i)
    					visited[i] = True
    	return ans
        
