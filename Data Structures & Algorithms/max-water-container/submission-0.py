class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left = 0
        right = len(heights) - 1 
        res = 0


        while left < right:
            w = right - left
            h = min(heights[left], heights[right])
            res = max(res, w * h)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return res