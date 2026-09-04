class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        [ intuition ]

        '''
        
        # backtrack x 2D-dp, time: O(n * 2^n), space: O(n^2)


        n = len(s)
        res = []
        
        # initialize 2d dp
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True

        # def backtrack method
        def dfs(start: int, cur_arr: list) -> None:
            # base
            if start == n:
                res.append(cur_arr[:])
                return
            
            # layer logic
            for i in range(start, n):
                if dp[start][i]:
                    cur_arr.append(s[start:i+1])
                    dfs(i + 1, cur_arr)
                    cur_arr.pop()

        # run the method
        dfs(0, [])
        return res