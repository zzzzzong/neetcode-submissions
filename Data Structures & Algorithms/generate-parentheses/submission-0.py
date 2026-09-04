class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
        [ intuition ]
        if any moment, right parentheses' amount is more than left, its invalid.

        define left_more meant the right - left amount
        '''
        res = []

        def backtrack(left_more: int, arr: list) -> None:
            # base
            if left_more < 0:
                return
            if len(arr) == 2 * n:
                if left_more == 0:
                    res.append(''.join(arr))
                return

            # try add left and right
            arr.append('(')
            backtrack(left_more + 1, arr)
            arr.pop()

            arr.append(')')
            backtrack(left_more - 1, arr)
            arr.pop()


            return


        backtrack(0, [])
        return res