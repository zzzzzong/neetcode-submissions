# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -float('inf')

        def helper(node: TreeNode | None) -> int:
            if not node:
                return 0
            
            left_path = max(0, helper(node.left))
            right_path = max(0, helper(node.right))

            self.max_sum = max(self.max_sum, left_path + right_path + node.val)

            return node.val + max(left_path, right_path)
        
        helper(root)

        return self.max_sum