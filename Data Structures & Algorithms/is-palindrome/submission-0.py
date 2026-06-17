class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [i.lower() for i in s if i.isalnum()]

        left = 0
        right = len(ss) - 1

        while left < right:
            if ss[left] != ss[right]:
                return False
            left += 1
            right -= 1
        
        return True