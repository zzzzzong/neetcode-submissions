class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ascii_counter = [False] * 256
        left = 0
        ans = 0

        for right in range(len(s)):
            right_ascii = ord(s[right])
            
            while ascii_counter[right_ascii]:
                left_ascii = ord(s[left])
                ascii_counter[left_ascii] = False
                left += 1
            
            ascii_counter[right_ascii] = True

            if ans < right - left + 1:
                ans = right - left + 1
		
        return ans