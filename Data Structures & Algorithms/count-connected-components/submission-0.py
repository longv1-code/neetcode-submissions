class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        res = 0
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(node, prior):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adjList[node]:
                if nei != prior:
                    dfs(nei, node)
            
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                res += 1
        
        return res