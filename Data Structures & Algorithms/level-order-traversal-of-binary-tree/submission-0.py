# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        hmap = {}

        def helper(node: TreeNode | None, height: int) -> None:
            if not node:
                return
            
            if height not in hmap:
                hmap[height] = [node.val]
            else:    
                hmap[height].append(node.val)
            
            helper(node.left, height + 1)
            helper(node.right, height + 1)

        helper(root, 0)
        for i in hmap:
            res.append(hmap[i])
        return res