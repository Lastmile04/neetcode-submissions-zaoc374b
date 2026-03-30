# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return False
        
        if not root:
            return False
        
        def same(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return same(r.left, s.left) and same(r.right, s.right)

        q = deque([root])

        while q:
            node = q.popleft()

            if node.val == subRoot.val:
                if same(node, subRoot):
                    return True
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        return False
