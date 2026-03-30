class Solution:
    # initialize dfs with state
    def dfs(self, r , c, grid):
        if ( r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == '0'):
            return
        
        grid[r][c] = "0"
        self.dfs(r+1, c, grid)
        self.dfs(r-1, c, grid)
        self.dfs(r, c+1, grid)
        self.dfs(r, c-1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:

        # the number of islands
        islands = 0   
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(r, c, grid)
                    islands += 1
            
        return islands