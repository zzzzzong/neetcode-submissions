class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # amount of banana eating each time
        ans = max(piles)

        while left <= right:
            mid = left + (right - left) // 2  # each time eats 'mid' banana

            # calculate the time would cost by this eating speed
            time = 0
            for p in piles:
                time += (p // mid)
                if p % mid != 0:
                    time += 1
            
            if time > h:
                left = mid + 1
                continue
            
            if mid < ans:
                ans = mid
            
            right = mid - 1



        return left