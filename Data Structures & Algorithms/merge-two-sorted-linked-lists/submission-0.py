# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values =[]
        curr = list1
        while curr:
            values.append(curr.val)
            curr = curr.next

        curr = list2
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        values.sort()
        dummy = ListNode(0)
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr=curr.next
        return dummy.next



