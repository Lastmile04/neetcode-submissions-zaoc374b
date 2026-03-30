class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] 
        cols = set()
        negDiag = set()     # row - col
        posDiag = set()     # row + col
        path = []           # path[row] = col

        def build_board():
            board = []
            for col in path:
                row_str = ['.'] * n
                row_str[col] = 'Q'
                board.append("". join(row_str))
            return board

        def dfs(row):
            # base case
            if row == n:
                res.append(build_board())
                return

            for col in range(n):
                pos = row + col
                neg  = row - col
                # constraints
                if col in cols or (row - col) in negDiag or (row + col) in posDiag:
                    continue
                
                # place queen and update kill zones
                path.append(col)
                cols.add(col)
                posDiag.add(pos)
                negDiag.add(neg)

                # recurse the choice go to the depth
                dfs(row + 1)

                # undo choice for the next choice and undo killzones
                path.pop()
                cols.remove(col)
                posDiag.remove(pos)
                negDiag.remove(neg)

        dfs(0)
        return res

                
