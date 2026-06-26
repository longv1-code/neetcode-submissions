class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        visiting = set()

        for crc, pre in prerequisites:
            preMap[crc].append(pre)

        def dfs(crc):
            if crc in visiting:
                return False
            if preMap[crc] == []:
                return True

            visiting.add(crc)
            for pre in preMap[crc]:
                if not dfs(pre):
                    return False
            visiting.remove(crc)
            preMap[crc] = []
            return True
    
        for c in range(numCourses):
            if not dfs(c):
                return False

        return True