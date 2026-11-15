/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type Set map[*ListNode]struct{}

func hasCycle(head *ListNode) bool {
	if head == nil{
		return false
	}

	visited := make(Set)

	for head != nil{
		if _, exists := visited[head]; exists{
			return true
		}
		visited[head] = struct{}{}
		head = head.Next
	}
	return false
}
