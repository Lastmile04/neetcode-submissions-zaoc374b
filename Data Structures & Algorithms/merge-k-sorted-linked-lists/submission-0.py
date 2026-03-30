# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        tail = dummy
        for k in range(len(lists)):
            if lists[k]:
                heapq.heappush(heap, (lists[k].val, k, lists[k]))
        
        while heap:
            val, k, node = heapq.heappop(heap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(heap, (node.next.val, k, node.next))

        return dummy.next