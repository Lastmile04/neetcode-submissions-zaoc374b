# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        nxtGrp = dummy
        prevGrp = dummy
        prevGrp.next = head
    
        while True:
            kNode = prevGrp.next
            for _ in range(k):
                if not kNode:
                    return dummy.next
                kNode = kNode.next


            nxtGrp = kNode

            prev, curr = nxtGrp, prevGrp.next
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # new head of the old grp
            tail = prevGrp.next
            prevGrp.next = prev
            prevGrp = tail

