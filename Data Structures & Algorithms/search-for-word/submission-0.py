from collections import Counter

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_count = Counter(char for row in board for char in row)
        word_count = Counter(word)

        for i in word_count:
            if word_count[i] > board_count[i]:
                return False
        
        if word_count[word[-1]] < word_count[word[0]]:
            word = word[::-1]


        def backtrack(r: int, c: int, i: int) -> bool:
            if i == len(word):
                return True

            if (r < 0 or r > len(board) - 1 or
                c < 0 or c > len(board[0]) - 1 or
                board[r][c] != word[i]):
        
                return False
            
            board[r][c] = '#'
            res = (backtrack(r + 1, c, i + 1) or
                   backtrack(r - 1, c, i + 1) or
                   backtrack(r, c + 1, i + 1) or
                   backtrack(r, c - 1, i + 1))
            board[r][c] = word[i]

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):

                if backtrack(r, c, 0):
                    return True
        return False