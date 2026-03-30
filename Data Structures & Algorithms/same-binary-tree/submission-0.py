# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # Both null -> same
            if not q and not p:
                return True
            
            # One null -> different 
            if not p or not q:
                return False
            
            # value different 
            if p.val != q.val:
                return False
            
            # Recursion children 
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

