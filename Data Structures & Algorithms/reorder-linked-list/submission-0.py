# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s,f = head, head
        while f and f.next:
            s=s.next
            f=f.next.next
        # Found the middle and store it
        half = s.next
        s.next = None

        # reverse the remaning half of list
        prev = None 
        curr = half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # merge two lists
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first, second = temp1, temp2