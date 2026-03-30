class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the number of islands
        islands = 0
        # define boundaries for row and col for grid problem
        rows, cols = len(grid), len(grid[0])
        # directions needed to be traversed
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        # initialize bfs with state
        def bfs(r,c):
            # initialize queue
            q = deque()
            # mark the current cell as water to indicated it's visted and prevent duplication
            grid[r][c] = '0'
            # append parms for later processing
            q.append((r,c))

            # loop non empty queue
            while q:
                # pop the params for processing
                row, col = q.popleft()
                # get the traversable neighbours
                for dr, dc in directions:
                    # add the directions to the current row and col, coordinates of neighbouring land
                    nr, nc = dr + row, dc + col
                    # skip the neightbours one with water or out of bound ones,  
                    if ( nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] == '0'):
                        continue
                    # append the neighbour for further iterative process that pass the filter 
                    q.append((nr,nc))
                    grid[nr][nc] = "0"
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
            
        return islands