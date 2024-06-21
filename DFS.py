def dfsOfGraph(self, V, adj):
        visited = [False] * V
        # visited[0] = True
        ans = []
        # ans.append(0)
        
        def dfs(adj, v, visited, ans):
            visited[v] = True
            ans.append(v)
            for i in adj[v]:
                if not visited[i]:
                    dfs(adj, i, visited, ans)
        dfs(adj, 0, visited, ans)
        return ans
