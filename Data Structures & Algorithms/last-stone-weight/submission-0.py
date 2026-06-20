class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        for i, x in enumerate(stones):
            stones[i] = -x

        heapq.heapify(stones)

        while len(stones) > 1:
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)
            res = abs(y - x)

            if res > 0:
                heapq.heappush(stones, -res)
        
        return -stones[0] if stones else 0