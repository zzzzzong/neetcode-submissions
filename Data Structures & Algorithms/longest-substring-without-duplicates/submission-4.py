class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.discard(s[left])
                left += 1
            
            char_set.add(s[right])
            
            if ans < right - left + 1:
                ans = right - left + 1
            
        return ans