class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        when we find a cycle, we find the edges, and see which one is last in the input and return
        '''
        n = len(edges)
        adjList = [[] for _ in range(n + 1)]

        def dfs(node, prior):
            if visiting[node]:
                return True

            visiting[node] = True
            for nei in adjList[node]:
                if nei != prior:
                    if dfs(nei, node):
                        return True
            
            return False

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

            visiting = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]

        return []