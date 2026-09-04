# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        '''
        [ intuition ]

        for every segment, the structure should looks like this:

        prev_end    [left, right]    nxt_start

        '''
        if not head: return None

        dummy = ListNode(0, head)
        reviewed = dummy
        nxt_start = head

        while nxt_start:
            # ensure there's enough nodes to reverse
            for _ in range(k):
                if not nxt_start:
                    return dummy.next
                nxt_start = nxt_start.next 

            # reverse the clip
            prev = nxt_start
            cur = reviewed.next
            end_of_clip = cur

            while cur != nxt_start:
                tmp = cur.next
                cur.next = prev
                if tmp == nxt_start:
                    reviewed.next = cur
                    break
                prev = cur
                cur = tmp

            while reviewed != end_of_clip:
                reviewed = reviewed.next


        return dummy.next


