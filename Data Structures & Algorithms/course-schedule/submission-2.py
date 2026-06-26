class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque

        indegree = [0] * numCourses # list of nodes' indegrees
        adj = [[] for i in range(numCourses)] # adjacency list
        for src, dst in prerequisites:
            indegree[dst] += 1 # for each src going to dst, increment the indegree
            adj[src].append(dst) # add dst in src's adjacency

        q = deque()
        for n in range(numCourses): # find sources
            if indegree[n] == 0:
                q.append(n)

        finish = 0
        while q:
            node = q.popleft() # pop a source
            finish += 1
            for nei in adj[node]: # look through source neighbors
                indegree[nei] -= 1 # decrement their indegree by one since we visited one of their sources
                if indegree[nei] == 0: # add new sources to queue
                    q.append(nei)

        return finish == numCourses # check for disconnect nodes or cycle