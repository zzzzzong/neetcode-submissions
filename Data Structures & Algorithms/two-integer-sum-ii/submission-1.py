class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers

        left = 0
        right = len(numbers) - 1

        while left < right:
            add_up = numbers[left] + numbers[right] 
            if add_up == target:
                return [left + 1, right + 1]

            elif add_up < target:
                left += 1
            else:
                right -= 1