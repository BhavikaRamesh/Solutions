#Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        # Code here
        indegree = [0] * V
        for i in range(V):
            if adj[i]:
                for v in adj[i]:
                    indegree[v] += 1
        q = deque()
        for i in range(V):
            if indegree[i] == 0:
                q.append(i)
        result = []
        while q:
            elem = q.popleft()
            result.append(elem)
            for i in adj[elem]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if len(result) != V:
            return []
        return result
