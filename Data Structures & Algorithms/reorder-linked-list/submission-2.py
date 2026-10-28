# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
            
        # 2. 利用雙指標（頭尾指標）直接在陣列裡交錯縫合，完全不浪費時間
        left, right = 0, len(nodes) - 1
        
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            
            # 如果兩個指標碰頭了，代表接完了，直接跳出
            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        # 最後一個節點的 next 記得切斷，避免環狀鏈結（Cycle）
        nodes[left].next = None