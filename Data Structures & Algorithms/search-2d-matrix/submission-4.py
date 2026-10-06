class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, rows - 1

        while left <= right:
            mid = left + (right - left) // 2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] > target:
                right = mid - 1
                continue
            left = mid + 1

        possible_row = right

        if possible_row < 0:
            return False


        left, right = 0, cols - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[possible_row][mid] == target:
                return True

            if matrix[possible_row][mid] < target:
                left = mid + 1
                continue
            right = mid - 1

            
        return False