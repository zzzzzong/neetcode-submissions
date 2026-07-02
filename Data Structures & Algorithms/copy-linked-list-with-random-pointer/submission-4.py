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
        # weaving and unweaving, time: O(3n) = O(n), space = O(1)

        
        # weaving the empty nodes alternatively in the list
        if not head:
            return None
        
        cur = head
        while cur:
            next_hop = cur.next
            cur.next = Node(cur.val, next_hop)
            cur = next_hop
        
        # dealing with the 'random' pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        
        # dealing with the 'next' pointer
        old_cur = head
        new_cur = head.next
        res = head.next
        
        while old_cur:
            old_cur.next = old_cur.next.next
            
            if new_cur.next:
                new_cur.next = new_cur.next.next
            else:
                new_cur.next = None
                
            old_cur = old_cur.next
            new_cur = new_cur.next
            
        return res