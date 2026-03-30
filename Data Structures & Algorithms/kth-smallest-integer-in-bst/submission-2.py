# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS
        stack = []
        node = root
        count = 0
        while stack or node:
            # go as left as possible
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            count +=1
            if count == k:
                return node.val
            # go as right as possible
            node = node.right


