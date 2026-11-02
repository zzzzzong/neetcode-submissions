# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        l2 = slow.next
        slow.next = None
        l1 = head

        # reverse
        prev = None
        cur_2 = l2

        while cur_2:
            cur_2.next, prev, cur_2 = prev, cur_2, cur_2.next

        l2 = prev

        # merge
        res = ListNode()
        cur = res
        while l2:
            next_1, next_2 = l1.next, l2.next

            l1.next = l2
            l2.next = next_1
            
            l1, l2 = next_1, next_2
        
        
        return res.next