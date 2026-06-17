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
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)

        return self.helper(root, min_val, max_val)
    

    def helper(self, node: Optional[TreeNode], min_val: int, max_val:int) -> Optional[TreeNode]:
        if min_val <= node.val <= max_val:
            return node
        
        if node.val > max_val:
            return self.helper(node.left, min_val, max_val)
        if node.val < min_val:
            return self.helper(node.right, min_val, max_val)