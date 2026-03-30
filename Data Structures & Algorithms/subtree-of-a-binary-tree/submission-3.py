# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        if not subRoot:
            return True

        def serialize(r):
            res = []

            def dfs(r):
                # base case
                if not r:
                    res.append('N')
                    return 

                res.append(str(r.val))
                dfs(r.left)
                dfs(r.right)

            dfs(r)
            return ",".join(res)

        root_str = serialize(root)
        sub_str = serialize(subRoot)

        return sub_str in root_str

