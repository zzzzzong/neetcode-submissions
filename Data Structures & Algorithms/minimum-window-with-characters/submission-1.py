from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        window_count = {}
        
        required = len(t_count)
        formed = 0
        
        ans = float("inf"), 0, 0
        left = 0
        
        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1
            
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                removed_char = s[left]
                window_count[removed_char] -= 1
                
                if removed_char in t_count and window_count[removed_char] < t_count[removed_char]:
                    formed -= 1
                
                left += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2]+1]
