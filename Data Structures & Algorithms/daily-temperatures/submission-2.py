class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [(temperatures[0], 0)]
        ans = [0] * n

        for i in range(1, n):
            while stack and temperatures[i] > stack[-1][0]:
                day = stack.pop()
                ans[day[1]] = i - day[1]

            stack.append((temperatures[i], i))

        return ans