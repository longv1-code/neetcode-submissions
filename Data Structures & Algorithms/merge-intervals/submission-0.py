class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sortIntervals = sorted(intervals, key=lambda x: x[0])

        res = [sortIntervals[0]]
        for i in range(1, len(sortIntervals)):
            if res[-1][0] <= sortIntervals[i][0] <= res[-1][1]:
                start, end = res.pop()
                res.append([start, max(end, sortIntervals[i][1])])
            else:
                res.append(sortIntervals[i])

        return res