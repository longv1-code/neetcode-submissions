class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        from math import sqrt

        res = []
        distToPt = {} # { distance : [points] }
        heap = []

        for x, y in points:
            distance = sqrt(x**2 + y**2)
            
            if distance not in distToPt:
                distToPt[distance] = [[x, y]]
            else:
                distToPt[distance].append([x, y])
            
            heapq.heappush(heap, -distance)

            if len(heap) > k:
                heapq.heappop(heap)

        for distance in heap:
            x, y = distToPt[-distance].pop()
            res.append([x, y])
        
        return res