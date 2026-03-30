class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the number of islands
        islands = 0
        # define boundaries for row and col for grid problem
        rows, cols = len(grid), len(grid[0])
        # directions needed to be traversed
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # initialize bfs with state
        def dfs(r,c):
            if ( r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
                return
            
            grid[r][c] = "0"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
            
        return islands