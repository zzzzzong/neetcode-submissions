class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we don't need to find the amount of banana, doesn't matter here.
        
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
        
            if self.can_eat_all(mid, piles, h):
                right = mid
            else:
                left = mid + 1
        
        return left

    def can_eat_all(self, speed: int, piles: list[int], guard_back: int) -> bool:
        cost_time = 0
        for p in piles:
            cost_time += (p + speed - 1) // speed   # make it over a bit but not enough 
            
        return cost_time <= guard_back