# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSame(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
 
            return isSame(p.left, q.left) and isSame(p.right, q.right)

        # 只要三者之一成立即可：
        # 1. 以目前節點為頭，兩棵樹長得一樣
        # 2. 或是在左子樹找找看
        # 3. 或是在右子樹找找看
        return isSame(root, subRoot) or \
               self.isSubtree(root.left, subRoot) or \
               self.isSubtree(root.right, subRoot)