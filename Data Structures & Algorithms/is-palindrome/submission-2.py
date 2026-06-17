class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # 左指標遇到非英數就往右跳過
            while left < right and not s[left].isalnum():
                left += 1
            # 右指標遇到非英數就往左跳過
            while left < right and not s[right].isalnum():
                right -= 1
                
            # 比對兩者的小寫是否相同
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True