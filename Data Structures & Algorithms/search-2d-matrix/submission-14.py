class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = matrix[0]
        for i in range(1, len(matrix)):
            arr.extend(matrix[i])
        
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            cur = arr[mid]

            if cur == target:
                return True
            if cur < target:
                left = mid + 1
                continue
            right = mid - 1
        
        return False