class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iterate, time: O(nlogn), space: O(n)

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        fleets = 1
        prev_time = (target - pair[0][0]) / pair[0][1]
        
        for i in range(1, len(pair)):
            cur_car = pair[i]
            cur_time = (target - cur_car[0]) / cur_car[1]
            if cur_time > prev_time:
                fleets += 1
                prev_time = cur_time
                
        return fleets