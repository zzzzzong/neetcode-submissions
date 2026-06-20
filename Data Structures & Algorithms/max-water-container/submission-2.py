class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right = n - 1

        max_water = 0

        while left < right:
            shorter = min(heights[left], heights[right])
            cur_water =  shorter* (right - left)
            
            max_water = max(max_water, cur_water)

            if shorter == heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_water