class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # brute force
        # time O(n ^ 2), space O(n)
        
        n = len(temperatures)
        res = []

        for left in range(n):
            for right in range(left + 1, n):
                if temperatures[left] < temperatures[right]:
                    res.append(right - left)
                    break
                
                elif right == n - 1:
                    res.append(0)
                else:
                    pass
        
        res.append(0)
        
        return res