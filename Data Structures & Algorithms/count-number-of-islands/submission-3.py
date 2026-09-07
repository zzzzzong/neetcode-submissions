from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # graph x bfs, time: O(m*n), space: O(m*n)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        rows, cols = len(grid), len(grid[0])
        res = 0

        def bfs(r: int, c: int) -> None:
            queue = deque()
            grid[r][c] = '0'
            queue.append((r, c))
            
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc

                    if (new_r < 0 or 
                        new_c < 0 or
                        new_r >= rows or
                        new_c >= cols or
                        grid[new_r][new_c] == '0'):
                        continue
                    
                    queue.append((new_r, new_c))
                    grid[new_r][new_c] = '0'
            

        # run main
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        
        return res