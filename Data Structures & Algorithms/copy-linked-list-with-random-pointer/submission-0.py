"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        original = {}

        prev = dummy
        curr = head

        while curr:
            new_node = Node(curr.val)
            original[curr] = new_node
            prev.next = new_node
            prev = new_node
            curr = curr.next

        newHead = dummy.next
        
        # PASS 2: Wire RANDOM pointers
        curr_old = head
        curr_new = newHead
        while curr_old:
            curr_new.random = original.get(curr_old.random)  # Safe None
            curr_old = curr_old.next
            curr_new = curr_new.next
        
        return dummy.next

            
