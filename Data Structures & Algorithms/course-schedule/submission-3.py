class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        indegree = [0] * numCourses
        adjList = [[] for _ in range(numCourses)]
        q = deque()

        for src, dst in prerequisites:
            indegree[dst] += 1
            adjList[src].append(dst)

        for node in range(numCourses):
            if indegree[node] == 0:
                q.append(node)
        
        finish = 0
        while q:
            node = q.popleft()
            finish += 1

            for n in adjList[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
            
        return finish == numCourses