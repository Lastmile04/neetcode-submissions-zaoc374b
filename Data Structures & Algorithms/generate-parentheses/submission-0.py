class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(openN, closeN):
            # BASE CASE
            if openN == n and closeN == n:
                res.append("".join(path))
                return

            # CHOICES
            # ADD (
            if openN < n:
                path.append("(") # choice
                dfs(openN + 1, closeN) # getting result from the choice 
                path.pop() # undo
            # ADD )
            if closeN < openN:
                path.append(")") # choice
                dfs(openN, closeN + 1) # getting result with that choice
                path.pop() # undo
        dfs(0,0)
        return res

