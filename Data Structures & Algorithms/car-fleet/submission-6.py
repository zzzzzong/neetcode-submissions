class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        [ intuition ]
        We only concern about the time for each car would cost to arrive target.
        If the car behind would arrived target with shorter time, means a car merge would happend.
        '''
        
        # initialize the varialbes
        n = len(speed)
        ans = n
        fleet = []

        for i in range(n):
            fleet.append((position[i], speed[i]))
        fleet.sort(reverse=True)
        

        # time = (target - position) / speed
        cur_lead_time = (target - fleet[0][0]) / fleet[0][1]
        
        for i in range(1, n):
            behind_time = (target - fleet[i][0]) / fleet[i][1]
            
            if behind_time > cur_lead_time:
                cur_lead_time = behind_time
                continue
            
            ans -= 1
        
        return ans
