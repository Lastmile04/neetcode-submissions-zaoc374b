class Solution:

    def bfs(self, r, c, grid):

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        q = deque([(r,c)])
        grid[r][c] = 0
        area = 0
        
        while q:
            row, col = q.popleft()
            area += 1
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if ( nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == 0):
                    continue
                
                q.append((nr, nc))
                grid[nr][nc] = 0
                
        
        return area

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, self.bfs(r, c, grid))
        return maxArea
            