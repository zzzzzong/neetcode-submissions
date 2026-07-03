# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode | None, cur_max_val: int) -> None:
            if not node:
                return 0
            
            is_good = 0
            if node.val >= cur_max_val:
                is_good = 1
                cur_max_val = node.val  # 直接更新，省去 max() 的開銷
            
            return is_good + dfs(node.left, cur_max_val) + dfs(node.right, cur_max_val)
            
        return dfs(root, root.val)