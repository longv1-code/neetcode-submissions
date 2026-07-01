class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) == 0:
            return True

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visiting = set()
        def dfs(node, prior):
            if node in visiting:
                return False
            if adj[node] == []:
                return True

            visiting.add(node)
            for nei in adj[node]:
                if nei == prior:
                    continue
                if not dfs(nei, node):
                    return False
            visiting.remove(node)
            adj[node] = []
            return True

        dfs(edges[0][0], -1)
        for i in range(len(adj)):
            if adj[i]:
                return False
        return True