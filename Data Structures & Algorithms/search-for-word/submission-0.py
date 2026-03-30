class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # BASE CASE
            if i == len(word):
                return True
            
            # constraints
            if (
                min(r,c) < 0 or             # lower bounds
                r >= ROWS or c >= COLS or     # upper bounds
                word[i] != board[r][c] or      # curr char not match
                (r,c) in path
                ):             # curr r or c is visited element in curr path
                    return False
            
            # choice
            path.add((r,c))
            res = (
                dfs(r+1, c, i+1) or   # DOWN
                dfs(r-1, c, i+1) or   # UP
                dfs(r, c+1, i+1) or   # RIGHT
                dfs(r, c-1, i+1)      # LEFT 
                )     
            path.remove((r,c))  # undo
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
