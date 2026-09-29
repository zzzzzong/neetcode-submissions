class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights) - 1

        while left < right:
            h = min(heights[left], heights[right])
            water = (right - left) * h
            if ans < water:
                ans = water
            
            if h == heights[left]:
                left += 1
                while left < right and heights[left] <= h:
                    left += 1
                continue
            
            while left < right and heights[right] <= h:
                right -= 1
        
        return ans