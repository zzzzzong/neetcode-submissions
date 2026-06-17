# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # fast slow

        if not head or not head.next:
            return
        
        # 1. 找中點 (你的快慢指標邏輯很好)
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 切開並反轉後半段
        second_half = slow.next
        slow.next = None  # 這是你提到的「斷開」
        
        l2 = self.reverse(second_half) # 呼叫reverse function
        l1 = head
    
        return self.merge_two_lists(l1, l2)


    def reverse(self, node: Optional[ListNode]) -> Optional[ListNode]:
        prev = None

        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        
        return prev
    
    def merge_two_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        while l2: # 因為l2長度一定會 <= l1
            tmp1, tmp2 = l1.next, l2.next
            
            l1.next = l2
            l2.next = tmp1
            
            l1, l2 = tmp1, tmp2
