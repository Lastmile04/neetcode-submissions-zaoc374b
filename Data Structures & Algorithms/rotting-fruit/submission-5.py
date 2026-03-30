"""
<!--Describe my first thoughts about this problem -->
-> traverse the graph and find the rotton friuts append these fruits to the queue first before processing them layer by layer alomost 90% similar to the wall and gate problem
 like in that problem we had find the nearest distance we can do the same in this increment time by one for each layer since we do not need to return an altered grid, instead 
 we just need to return the time taking for every fruit to turn rotton
 -> we keep increasing the value of each cell we traverse when the entire grid is traversed we get the last changed cell and return the result by subtracting 2 from it's value
 update the last changed every iteration
 -> handle the edge case of rotton fruit not having any fresh fruit adjacent to it, for it to rot and most importantly if all the fresh fruits are not rotton return -1
<--Complexity-->
Time: O(r + c) because even if you start at multiple sources each element inside every row col pair is visited at most once
Space: O(r)

"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        time = 0
        fresh_count = 0
        
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh_count +=1

        # stop wasteful continuation of loop when no fresh fruits are left
        while q and fresh_count > 0:
            time+=1
            for _ in range(len(q)):
                # process current level
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh_count-=1
                    q.append((nr, nc))
            

        # some fresh fruits still left
        if fresh_count > 0: return -1
        return time 
        