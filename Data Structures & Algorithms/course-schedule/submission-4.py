class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        q = deque()

        for src, dst in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for nei in adjList[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return finish == numCourses