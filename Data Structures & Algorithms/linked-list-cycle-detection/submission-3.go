/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type Set map[int]struct{}

func hasCycle(head *ListNode) bool {
	if head == nil{
		return false
	}
	
	unique := make(Set)

	for head.Next != nil{
		if _, exists := unique[head.Val]; exists{
			return true
		}
		unique[head.Val] = struct{}{}
		head = head.Next
	}
	return false
}
