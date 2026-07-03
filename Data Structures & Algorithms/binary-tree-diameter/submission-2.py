# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Thread-Safety: Eliminates shared states like self.res. 
        # This prevents race conditions when multiple threads execute the function simultaneously.
        # No Side Effects: Functions as a pure function. 
        # It does not modify object properties, making it highly reliable and much easier to isolate for unit testing.
        self.res = 0

        def dfs(node: TreeNode | None) -> tuple[int, int]:
            if not node:
                return 0, 0

            left_depth, left_dia = dfs(node.left)
            right_depth, right_dia = dfs(node.right)

            current_dia = left_depth + right_depth
            max_dia = max(current_dia, left_dia, right_dia)
            current_depth = 1 + max(left_depth, right_depth)

            return current_depth, max_dia

        _, total_max_diameter = dfs(root)
        return total_max_diameter