class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers

        # initialize
        water = 0
        left, right = 0, len(height) - 1
        left_highest, right_highest = 0, 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_highest:
                    left_highest = height[left]
                else:
                    water += left_highest - height[left]

                left += 1

            else:
                if height[right] >= right_highest:
                    right_highest = height[right]
                else:
                    water += right_highest - height[right]

                right -= 1

        return water