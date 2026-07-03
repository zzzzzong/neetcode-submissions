# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # dfs (optimaized), time: O(n), space: O(H) = O(logn)
        def dfs(node: TreeNode | None) -> int:
            # 說明：回傳該子樹的深度。若子樹不平衡，則立刻回傳 -1
            if not node:
                return 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1  # 左子樹不平衡，立刻剪枝回傳，不再計算右邊

            right_height = dfs(node.right)
            if right_height == -1:
                return -1  # 右子樹不平衡，立刻剪枝回傳

            # 檢查當前節點是否平衡
            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return dfs(root) != -1