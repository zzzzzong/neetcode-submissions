# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass, time: O(n), space: O(1)

        # count the number
        cur = head
        length = 0

        while cur:
            length += 1
            cur = cur.next
        
        # traverse and remove the node
        dummy = ListNode(0, head)
        cur = dummy

        while cur:
            if length - n == 0:
                cur.next = cur.next.next

            cur = cur.next
            n += 1

        return dummy.next