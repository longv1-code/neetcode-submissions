class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = []

        for curStart, curEnd in intervals:
            if not res:
                res.append([curStart, curEnd])
                continue
            prevStart, prevEnd = res.pop()
            if prevStart <= curStart <= prevEnd:
                res.append([prevStart, max(prevEnd, curEnd)])
            else:
                res.append([prevStart, prevEnd])
                res.append([curStart, curEnd])  
        return res
            