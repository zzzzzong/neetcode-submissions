class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # backtrack, time: O(4^n / sqrt(n)), space: O(n), where n is the number of pairs
        res = []

        def backtrack(left: int, right: int, arr: list) -> None:
            if left == 0 and right == 0:
                res.append(''.join(arr))
                return

            if left > 0:
                arr.append('(')
                backtrack(left - 1, right, arr)
                arr.pop()

            if right > left:
                arr.append(')')
                backtrack(left, right - 1, arr)
                arr.pop()

        backtrack(n, n, [])
        return res