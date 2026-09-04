class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # greedy x backtrack, time: O(2^n), space: O(n)
        if not digits: return []

        map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        n = len(digits)

        def dfs(index: int, cur_arr: list) -> None:
            if index == n:
                res.append(''.join(cur_arr))
                return
            
            for letter in map[digits[index]]:
                cur_arr.append(letter)

                dfs(index + 1, cur_arr)

                cur_arr.pop()
        
        dfs(0, [])

        return res