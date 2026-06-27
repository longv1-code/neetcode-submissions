class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        res = 0
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjList[node]:
                if nei not in visited:
                    dfs(nei)
            
        for node in range(n):
            if node not in visited:
                dfs(node)
                res += 1

        
        return res