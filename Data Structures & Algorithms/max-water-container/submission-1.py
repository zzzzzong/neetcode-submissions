class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0
        
        while left < right:
            wall = min(heights[left], heights[right])
            water = (right - left) * wall
            max_water = max(max_water, water)

            if wall == heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_water