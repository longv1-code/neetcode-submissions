class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import deque

        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        q = deque()
        res = []

        for dst, src in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1

            for nei in adjList[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        return res if finish == numCourses else []