from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    self.bfs(grid, r, c, rows, cols)
                    ans += 1
        
        return ans
    
    def bfs(self, grid: List[List[str]], r: int, c: int, rows: int, cols: int) -> None: 
        queue = deque([(r, c)])

        while queue:
            r, c = queue.popleft()
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == '1'
                    ):

                    grid[nr][nc] = '0'
                    queue.append((nr, nc))
                    
                
            
        