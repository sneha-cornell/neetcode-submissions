class Solution:
    def maxArea(self, heights: List[int]) -> int:
       #array of integers input
       #output - max area of water (sits between 2 lines only)
       #move only shorter line inward 
       
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            width = r - l
            area = min(heights[l], heights[r]) * width
            best = max(best, area)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best
