class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        blocks = defaultdict(set)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                
                number = board[r][c]
                if (number in rows[r] or
                    number in cols[c] or
                    number in blocks[(r // 3, c // 3)]):

                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[r // 3, c // 3].add(board[r][c])

        return True