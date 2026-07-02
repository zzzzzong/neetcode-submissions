"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        cur = head
        hmap = {}

        while cur:
            hmap[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        res = hmap[cur]

        while cur:
            hmap[cur].next = hmap[cur.next] if cur.next else None
            hmap[cur].random = hmap[cur.random] if cur.random else None
            cur = cur.next
        
        return res