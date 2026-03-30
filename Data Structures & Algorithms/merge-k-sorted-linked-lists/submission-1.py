# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # handle edge case of list being empty
        if not lists:
            return None

        while len(lists)>1:
            merged_list = []
            # since we only need two k lists at a time 
            for k in range(0, len(lists), 2): #increment by 2
                l1 = lists[k]
                l2 = lists[k+1] if (k+1) < len(lists) else None #check the edge case of k being odd
                merged_list.append(self.mergeTwoLists(l1, l2))
            # update list var
            lists = merged_list
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2 # if l1 or l2 have any element left
        return dummy.next

            
         
