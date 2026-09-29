class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = []

        for i in range(len(s)):
            if s[i].isalnum():
                new_s.append(s[i].lower())

        left, right = 0, len(new_s) - 1

        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
                continue
            
            return False
        
        return True