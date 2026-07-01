class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # to ensure A is the shorter one
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        total_length = len(A) + len(B)
        half_length = (total_length + 1) // 2   # if it's odd, should take one more.

        # initialize the binary search
        left, right = 0, len(A)

        while left <= right:
            i = left + (right - left) // 2  
            j = half_length - i

            A_left = A[i - 1] if i > 0 else float('-inf')
            A_right = A[i] if i < len(A) else float('inf')
            
            B_left = B[j - 1] if j > 0 else float('-inf')
            B_right = B[j] if j < len(B) else float('inf')

            if A_left <= B_right and B_left <= A_right:
                # 情況 A：總長度為奇數，中位數在左半邊的最大值
                if total_length % 2 == 1:
                    return max(A_left, B_left)

                # 情況 B：總長度為偶數，中位數為左最大與右最小的平均值
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            
            elif A_left > B_right:
                # A 左邊拿太多了，鋸子要往左移
                right = i - 1
            else:
                # A 左邊拿太少了，鋸子要往右移
                left = i + 1
                
        return 0.0