# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])

        while q:
            lvl = []
            for _ in range(len(q)):
                node = q.popleft()
                lvl.append(node.val)
                if node.right: q.append(node.right)
                if node.left: q.append(node.left)
            res.append(lvl[0])

        return res




