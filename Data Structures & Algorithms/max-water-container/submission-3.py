class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            h_left = heights[left]
            h_right = heights[right]

            if h_left < h_right:
                cur_water = h_left * (right - left)
                if cur_water > max_water:
                    max_water = cur_water
                
                while left < right and heights[left] <= h_left:
                    left += 1
            
            else:
                cur_water = h_right * (right - left)
                if cur_water > max_water:
                    max_water = cur_water

                while left < right and heights[right] <= h_right:
                    right -= 1
                    
                         
        return max_water