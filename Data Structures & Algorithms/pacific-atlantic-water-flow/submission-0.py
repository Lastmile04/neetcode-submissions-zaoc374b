'''
-> Describe your first thoughts about this problem?
Seems like a traversal problem where we have to find out from which cell can water flow to both the bordering oceans, like if rain fell on each cell which cell
drain water to both pacific and atlantic, water can flow in 4 direction and only from high to low.

- One naive approach would be to do dfs on each cell to check if we can reach the top left and bottom right part of the grid but heights length can go upto 100
which might make it very inefficient, So have to think of another way as in the naive approach we might be exploring the visited cells multiple times

- the problems forces us to think in one way from cell to ocean, but we want to know if the flows upto the oceans from the cell we can follow the trail from the 
ocean upto the cells
- For this approach first we'll need the cells that border the oceans, top, bottom row and first and last column
Start with pacific ocean and from the border cells go uphill apply dfs/bfs to move towards uphill adjacent cells

-> Complextiy
- Time 
    O(M*N) even though we are only doing border cells in worst case we might end up visitng all the cells

- Space
    O(N) no new data structure used all changes made in place
'''


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])
        # directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]   later for bfs solution try

        # visited set of cells
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevHeight):
            # base case
            if ((r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            
            visited.add((r, c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # rows
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows - 1 , c, atlantic, heights[rows-1][c])
        
        # cols
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols - 1, atlantic, heights[r][cols-1])
        
        # result
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res
            

      
        


