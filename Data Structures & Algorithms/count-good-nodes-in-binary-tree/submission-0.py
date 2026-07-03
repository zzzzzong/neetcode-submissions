# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node: TreeNode | None, cur_max_val: int) -> None:
            if not node:
                return
            
            if node.val >= cur_max_val:
                self.res += 1
            
            next_max = max(cur_max_val, node.val)

            dfs(node.left, next_max)
            dfs(node.right, next_max)

        dfs(root, -101)

        return self.res