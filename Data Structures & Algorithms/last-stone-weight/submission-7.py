class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        if len(stones) == 1:
            return stones[0]

        heap = []
        
        for x in stones:
            heapq.heappush(heap, -x)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x - y != 0:
                heapq.heappush(heap, -abs(x - y))

        return -heap[0] if heap else 0