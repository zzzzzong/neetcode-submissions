class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        left, right = 0, len(heights) - 1

        while left < right:
            
            h = min(heights[left], heights[right])
            amount = h * (right - left)

            if amount > ans:
                ans = amount
            
            if heights[left] == h:
                left += 1
                continue
            right -= 1
        
        return ans