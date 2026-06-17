# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



'''
        1. DFS find these nodes first
        2. backtracking to find the LCA
        
        Note:
            Let's assume that p < q,

            Because it's a BST, so the LCA must in this interval: 
                p <= LCA < q
            due to the unique characteristic, LCA must not be q
'''

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a = min(p.val, q.val)
        b = max(p.val, q.val)

        while root:
            if a <= root.val <= b:
                return root

            elif root.val > b:
                root = root.left
            else:
                root = root.right
        