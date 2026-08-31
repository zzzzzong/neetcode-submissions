class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # initial variables
        res = []
        rows = len(board)
        cols = len(board[0])

        # build a trie
        tries = {}
        for i in words:
            cur = tries
            for j in i:
                if j not in cur:
                    cur[j] = {}
                cur = cur[j]
            cur['word'] = i

        # dfs design
        def dfs(r: int, c: int, cur_node: dict) -> None:
            # check the boundaries (修正變數名稱與換行)
            if r < 0 or r >= rows or \
               c < 0 or c >= cols or \
               board[r][c] == '#':
                return

            letter = board[r][c]

            # pruning 1
            if letter not in cur_node:
                return
                
            # go to the next layer
            next_node = cur_node[letter]

            # check if there's a word in next layer
            if 'word' in next_node and next_node['word'] is not None:
                res.append(next_node['word'])
                next_node['word'] = None    # key: Prevent duplicated count

            # tmp denote '#' sign
            board[r][c] = '#'

            # toward to 4 directions
            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)
            
            # recover the cell
            board[r][c] = letter

        # traversal
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, tries)
        
        return res
