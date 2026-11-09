class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter = set()
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] not in letter:
                letter.add(s[right])
                continue
            
            length = right - left
            if length > ans:
                ans = length

            while s[right] in letter:
                letter.discard(s[left])
                left += 1
        
            letter.add(s[right])
        
        k = len(letter)
        if k > ans:
            return k
        
        return ans