class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # counter, time: O(n), space: O(n)
        if len(s) != len(t):
            return False
        
        count_a, count_b = [0] * 26, [0] * 26

        for i in range(len(s)):
            count_a[ord(s[i]) - ord('a')] += 1
            count_b[ord(t[i]) - ord('a')] += 1

        return count_a == count_b