class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left <= right:
            mid = left + (right - left) // 2

            time = 0
            for p in piles:
                time += (p + mid - 1) // mid
            
            if time > h:
                left = mid + 1
                continue
            right = mid - 1

        return left