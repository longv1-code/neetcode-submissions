class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1
        area = 0

        while L < R:
            area = max(area, min(heights[R], heights[L]) * (R - L))

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1
        
        return area