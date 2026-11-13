from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = self.bfs(grid, i, j, m, n)
                    if area > ans:
                        ans = area

        return ans


    def bfs(self, grid: List[List[int]], r: int, c: int, rows: int, cols: int) -> int:
        queue = deque([(r, c)])
        grid[r][c] = 0
        area = 1


        while queue:
            r, c = queue.popleft()

            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    area += 1
                    queue.append((nr, nc))
        
        return area