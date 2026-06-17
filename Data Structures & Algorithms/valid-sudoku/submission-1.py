class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                cell = board[r][c]
                if cell == '.':
                    continue

                if (cell in rows[r] or
                    cell in cols[c] or
                    cell in blocks[(r // 3, c // 3)]):

                    return False
                
                rows[r].add(cell)
                cols[c].add(cell)
                blocks[(r // 3, c // 3)].add(cell)
        
        return True