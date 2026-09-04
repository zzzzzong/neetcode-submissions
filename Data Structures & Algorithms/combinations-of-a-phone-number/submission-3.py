class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # greedy x backtrack, time: O(n * 4^n), space: O(n)
        if not digits: return []
        
        if not digits:
            return []

        digit_map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        res = []
        n = len(digits)

        def dfs(index: int, cur_str: str) -> None:
            if index == n:
                res.append(cur_str)
                return
            
            for letter in digit_map[digits[index]]:
                dfs(index + 1, cur_str + letter)
        
        dfs(0, "")
        return res