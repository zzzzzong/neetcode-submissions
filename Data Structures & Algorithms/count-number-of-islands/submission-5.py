from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        
        def check(row: int, col: int) -> None:
            queue = deque([(row, col)])
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'
                        queue.append((nr, nc))             
        

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    ans += 1
                    check(i, j)
        
        return ans