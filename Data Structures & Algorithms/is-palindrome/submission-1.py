class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = "".join(i.lower() for i in s if i.isalnum())

        left = 0
        right = len(words) - 1

        while left < right:
            if words[left] != words[right]:
                return False
            left += 1
            right -= 1
        
        return True