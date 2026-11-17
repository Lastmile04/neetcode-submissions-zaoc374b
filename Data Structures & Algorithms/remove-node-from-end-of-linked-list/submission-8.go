/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	count:= 0
	length:=0
	curr:=head
	for curr !=nil{
		length++
		curr = curr.Next
	}
	if n == 1 && length == 1 {
		return nil
	}

	half := (length - n) + 1
	dummy:= &ListNode{Next: head}

	curr = head
	prev := dummy
	for curr!=nil{
		count++
		if count == half{
			prev.Next = curr.Next
			curr.Next = nil
		}
		curr = curr.Next
		prev = prev.Next
	}
	head = dummy.Next
	return head
}
