/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func hasCycle(head *ListNode) bool {
    check := make(map[*ListNode]bool)

    for head != nil {
        if _, ok := check[head]; ok {
            return true
        }
        check[head] = true
        head = head.Next
    }
    return false
}
