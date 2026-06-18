class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 2d binary search

        # outter
        left = 0
        right = len(matrix)

        the_row = 0

        while left < right:
            mid = left + (right - left) // 2

            if matrix[mid][0] == target or matrix[mid][-1] == target:
                return True
            
            elif matrix[mid][0] < target < matrix[mid][-1]:
                the_row = mid
                break
            
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        

        # inner
        left = 0
        right = len(matrix[the_row])

        while left < right:
            mid = left + (right - left) // 2

            if matrix[the_row][mid] == target:
                return True
            
            elif matrix[the_row][mid] < target:
                left += 1

            else:
                right -= 1
        
        return False