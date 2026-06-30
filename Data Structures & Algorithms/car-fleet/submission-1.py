class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack, time: O(nlogn), space: O(n)

        '''
        We just need to concern about the time that arrived the target.
        If the left-side car would arrived earlier than the right-side car,
        then they would be merged into one fleet.

        math formula derivation:
        - movement / speed = time
        - movemet = target spot - initial spot
        
        => (target - initial) / speed
        '''
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        stack = []
        
        for p, s in pair:
            stack.append((target - p)/ s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)