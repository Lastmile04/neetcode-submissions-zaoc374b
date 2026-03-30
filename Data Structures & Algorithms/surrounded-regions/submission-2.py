# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# the problem basically asks to spare the regoin which connected to the border and filp the ones that isn't or can say are "surrounded"

# Approach
# so i have to find the region, and find out if the current cell is at the edge
#  dfs or bfs traversal can do the traversal and as i am traversering i can mark the cell by checking if it's not a boundary cell

# the upper approach is too much work i can just find the cells/regions that are safe and just turn everything else to unsafe

# if the current cell is in boundary find it's region else just mark unsafe

# final polished approach mark the safe cells as S using dfs or bfs then in the main def mark the safe cells as back to O while mark the O/unsafe cells to X

# <!-- How can i tell if a cell is at the edge or not. -->
#  r == 0 or c == 0 or r == m-1 or c == n-1 (checks all the boundary element)

# time complexity
# space complexity


class Solution:
    
    # def bfs(self, r, c, board):
    #     directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    #     q = deque([(r, c)])
    #     rows, cols = len(board), len(board[0])
    #     board[r][c] = "S"

    #     while q:
    #         row, col = q.popleft()
    #         for dr, dc in directions:
    #             nr, nc = dr + row, dc + col

    #             if nr < 0 or nc < 0 or nr >= rows or nc >= cols or board[nr][nc] != "O":
    #                 continue

    #             board[nr][nc] = "S"
    #             q.append((nr,nc))

    def dfs(self, r, c, board):

        rows, cols = len(board), len(board[0])
        # base case
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
            return
        
        board[r][c] = 'S'
        self.dfs(r+1, c, board)
        self.dfs(r-1, c, board)
        self.dfs(r, c+1, board)
        self.dfs(r, c-1, board)
    
    def solve(self, board: List[List[str]]) -> None:
        
        if len(board) <= 1:
            return 
        
        rows, cols = len(board), len(board[0])
        # for cols
        for r in range(rows):
            # first col
            if board[r][0] == 'O':
                self.dfs(r, 0, board)
            # last col
            if board[r][cols-1] == 'O':
                self.dfs(r, cols-1, board)
            
        # for rows, skip already visited cells 
        for c in range(1, cols-1):
            # first row
            if board[0][c] == 'O':
                self.dfs(0, c, board)
            # last row
            if board[rows-1][c] == 'O':
                self.dfs(rows-1, c, board)

        # final pass, flip the safe cells back to orignal char, and unsafe land char to water char
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "S":
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'