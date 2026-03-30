# Approach
# <!-- Describe first impression of the problem -->
# INF is land that can be traversed, -1 is water so no passage there, 0 the treasure chest to find
# What we're supposed to do with this problem is: change the land value to the nearest distance to the treasure chest from that land
# if INF traverse and find the nearset 0, if -1 skip, if 0 skip 
# but check if land and traversing each time costs to much time and is a very inefficient and bad brute force way to think about it
# better is to just find the treasure cell first and then go outwards 

# for this particular approach we use multisource BFS, where we first find both the treasures and then start bfs from all the treasure cell at once and since queue processes
# cell in increasing distance order, the first time a cell is visited, it receives the shortest distance from the nearest gate. After that, we skip it using the INF check,
# preventing any overwriting.

# so the play here is to make the queue not limited to the scope of the bfs funtion and instead make it scope to the main funtion
# append all the treasure cells inside the queue and then call bfs once to get the correct distance as dicussed above

# complexity
# time 
# O(r+c) since there can be just land and no treasure chest

# Space
# O(r)

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = deque()
        INF = 2**31 - 1
          
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr+row, dc+col
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != INF:
                        continue
                    # I wasn't able to think of this logic on my own, have to improve that
                    # what we do is simple we add 1 to the previously visited cell incrementing the distance travelled by 1
                    grid[nr][nc] = grid[row][col] + 1
                    q.append((nr, nc))

        
