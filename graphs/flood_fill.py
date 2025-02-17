#Flood fill is a graph traversal algorithm that is used to fill a connected region with a new color.
#We will be given a grid and a starting point. We will be given a new color. We will be given a target color.

#Example:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]

#We will be given a grid and a starting point. We will be given a new color. We will be given a target color.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        initial_color = image[sr][sc]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        if initial_color == color:
            return image

        def dfs(r, c, image, color):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initial_color:
                return
            image[r][c] = color
            for dr, dc in directions:
                dfs(r + dr, c + dc, image, color)

        dfs(sr, sc, image, color)
        return image

#Time complexity: O(n*m) because we are iterating over each cell in the grid.
#Space complexity: O(n*m) because we are using a grid to store the image.

#BFS solution:
from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        initial_color = image[sr][sc]
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        if initial_color == color:
            return image

        def bfs(r, c, image, color):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != initial_color:
                return
            image[r][c] = color
            q = deque()
            q.append((r, c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == initial_color:
                        image[nr][nc] = color
                        q.append((nr, nc))
        bfs(sr, sc, image, color)
        return image

#Time complexity: O(n*m) because we are iterating over each cell in the grid.
#Space complexity: O(n*m) because we are using a queue to store the cells.
