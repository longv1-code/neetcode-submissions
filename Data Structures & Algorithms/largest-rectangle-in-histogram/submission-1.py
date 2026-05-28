class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        find largest rectangle from the histogram
        max height, max array length
        
        similar to trapping rain water problem
        area -> minimum height of the bars within the area inclusive * the distance between the two end bars
        pattern: 2 pointers
        approach:
        1. 
        brute force:
        nested for loops to calculate the area each time and take the max area
        '''
        maxArea = 0
        for i in range(len(heights)):
            currArea = 0
            currHeight = heights[i]
            j, k = i, i + 1
            while j >= 0 and currHeight <= heights[j]:
                currArea += currHeight
                j -= 1
            while k < len(heights) and currHeight <= heights[k]:
                currArea += currHeight
                k += 1
            maxArea = max(maxArea, currArea)
        
        return maxArea