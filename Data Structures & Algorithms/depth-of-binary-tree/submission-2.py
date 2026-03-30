# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # # bfs suing queue
        # q = deque()
        # if root:
        #     q.append(root)
        
        # level = 0

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level +=1
        # return level

        #dfs using stack
        stack = [[root, 1]]

        res = 0
        while stack:
            node, depth = stack.pop()

            if node:
                res = max(depth, res)
                stack.append([node.left, depth +1])
                stack.append([node.right, depth +1])

        return res
