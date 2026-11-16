/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reorderList(head *ListNode) {
    if head == nil || head.Next == nil{
		return
	}

	length := 0
	curr := head
	for curr != nil{
		length++
		curr = curr.Next
	}

	half := (length+1) / 2
	curr = head
	for pos := 1; pos < half; pos++{
		curr = curr.Next
	}

	secondHead := curr.Next
	curr.Next = nil

	secondHead = reverseList(secondHead)

	head1:= head
	head2:= secondHead

	for head2 != nil{
		temp1:=head1.Next
		temp2:=head2.Next

		head1.Next = head2
		head2.Next = temp1

		head1 = temp1
		head2 = temp2
	}	
}

func reverseList(head *ListNode) *ListNode {
    if head == nil {
		return nil
	}

	newHead := head
	if head.Next != nil {
		newHead = reverseList(head.Next)
		head.Next.Next = head
	}
	head.Next = nil

	return newHead
}