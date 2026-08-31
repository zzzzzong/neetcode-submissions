class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for r in range(n // 2):
            for c in range((n + 1) // 2):
                
                matrix[r][c], matrix[c][n - 1 - r], matrix[n - 1 - r][n - 1 - c], matrix[n - 1 - c][r] = \
                matrix[n - 1 - c][r], matrix[r][c], matrix[c][n - 1 - r], matrix[n - 1 - r][n - 1 - c]