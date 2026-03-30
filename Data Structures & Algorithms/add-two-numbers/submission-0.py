# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        prev = dummy
        carry = 0
        while l1 or l2 or carry:
            digit1 = 0
            digit2 = 0

            if l1: digit1 = l1.val
            if l2: digit2 = l2.val
            total = digit1 + digit2 + carry
            

            new_node = ListNode(total%10)
            carry = total//10

            prev.next = new_node
            prev = new_node

            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
            
