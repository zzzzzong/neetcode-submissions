from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    a = self.bfs(grid, i, j, m, n)
                    if a > ans:
                        ans = a
        
        return ans
        
    
    def bfs(self, arr: List[List[int]], r: int, c: int, rows: int, cols: int) -> int:
        queue = deque([(r, c)])
        arr[r][c] = 0
        area = 1

        while queue:
            r, c = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    arr[nr][nc] == 1
                ):
                    arr[nr][nc] = 0
                    area += 1
                    queue.append((nr, nc))
            
        return area