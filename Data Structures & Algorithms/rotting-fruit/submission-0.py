class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # bfs, time: O(rows * cols), space: O(rows * cols)
        ans = 0
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                    continue
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        
        while queue:
            r, c ,time = queue.popleft()
            if time > ans:
                ans = time
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 1
                ):
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))
        
        if fresh != 0:
            return -1
        
        return ans