from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        If we just directly check every cells would cause TLE.
        We gonna think reversely, think of " water flow from lower to higher "
        Then check if it caused two directions
        '''

        rows, cols = len(heights), len(heights[0])
        pacific_queue, atlantic_queue = deque(), deque()

        for r in range(rows):
            pacific_queue.append((r, 0))
            atlantic_queue.append((r, cols - 1))

        for c in range(cols):
            pacific_queue.append((0, c))
            atlantic_queue.append((rows - 1, c))

        pacific_reachable = self._bfs(pacific_queue, heights, rows, cols)
        atlantic_reachable = self._bfs(atlantic_queue, heights, rows, cols)

        return [list(coord) for coord in (pacific_reachable & atlantic_reachable)]

    def _bfs(
        self, queue: deque, heights: List[List[int]], rows: int, cols: int
    ) -> set:

        visited = set(queue)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and (nr, nc) not in visited
                    and heights[nr][nc] >= heights[r][c]
                ):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

        return visited