class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        left_highest, right_highest = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_highest:
                    left_highest = height[left]
                    left += 1
                    continue
                
                water += left_highest - height[left]
                left += 1
                continue

            if height[right] >= right_highest:
                right_highest = height[right]
                right -= 1
                continue

            water += right_highest - height[right]
            right -= 1

        return water