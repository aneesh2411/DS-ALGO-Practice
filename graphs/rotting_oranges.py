# we are given a grid of oranges. We are given a starting point. We are given a target point. We are given a rotten orange.

# Return the minimum number of minutes it takes for all the oranges to rot.

# Example:
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

#If Impossible, return -1.

#BFS Solution:

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh += 1
        if fresh == 0:
            return 0
        time = 0
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append((nr,nc))
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1

# DFS Solution:

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        rotten = []
        
        # Count fresh oranges and find rotten ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
        
        if fresh == 0:
            return 0
            
        def dfs(r, c, time):
            nonlocal fresh
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                return
                
            grid[r][c] = 2
            fresh -= 1
            
            # Mark time of rotting
            grid[r][c] = time + 2
            
            # Spread to neighbors
            dfs(r+1, c, time+1)
            dfs(r-1, c, time+1) 
            dfs(r, c+1, time+1)
            dfs(r, c-1, time+1)
        
        # Start DFS from each rotten orange
        for r,c in rotten:
            dfs(r+1, c, 1)
            dfs(r-1, c, 1)
            dfs(r, c+1, 1)
            dfs(r, c-1, 1)
            
        return -1 if fresh > 0 else max(max(row) for row in grid) - 2