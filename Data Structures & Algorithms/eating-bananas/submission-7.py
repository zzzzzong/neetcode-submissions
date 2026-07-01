class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def is_valid(speed: int, stacks: list[int]) -> bool:
            count = 0
            for p in stacks:
                count += (p + speed - 1) // speed
            
            return count <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if is_valid(mid, piles):
                right = mid
            else:
                left = mid + 1
        
        return left