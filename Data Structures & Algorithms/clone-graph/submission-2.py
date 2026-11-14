"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        ans = Node(node.val)
        hmap = {node: ans}

        queue = deque([node])

        while queue:
            cur = queue.popleft()

            for nei in cur.neighbors:
                if nei not in hmap:
                    hmap[nei] = Node(nei.val)
                    queue.append(nei)
                
                hmap[cur].neighbors.append(hmap[nei])
        
        return ans