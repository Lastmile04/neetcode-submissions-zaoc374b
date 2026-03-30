class Solution:
    # initialize dfs with state
    def dfs(self, r , c, grid):
        rows, cols = len(grid), len(grid[0])
        if ( r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'):
            return
        
        grid[r][c] = "0"
        self.dfs(r+1, c, grid)
        self.dfs(r-1, c, grid)
        self.dfs(r, c+1, grid)
        self.dfs(r, c-1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])
        # the number of islands
        islands = 0   
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid)
                    islands += 1
            
        return islands