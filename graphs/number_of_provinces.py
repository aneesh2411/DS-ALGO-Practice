#lets say we have a graph with n nodes and m edges. We want to find the number of provinces in the graph.
#A province is a connected component in the graph.
#We will be given an adjacency matrix.

# We have to find the number of connected components in the graph.

#Example:
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2


isConnected = [[1,1,0],[1,1,0],[0,0,1]]

#Recursive DFS solution:
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        provinces = 0

        def dfs(node, isConnected, seen):
            seen.add(node)
            for nei in range(n):
                if isConnected[node][nei] and nei not in seen:
                    seen.add(nei)
                    dfs(nei, isConnected, seen)
        
        for node in range(n):
            if node not in seen:
                provinces += 1
                dfs(node, isConnected, seen)
        return provinces
    
#Time complexity: O(n^2) because we are iterating over each node and each node has n neighbors.
#Space complexity: O(n) because we are using a set to keep track of visited nodes.


#BFS solution:

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        seen = set()
        provinces = 0

        def bfs(node, isConnected, seen):
            q = deque()
            q.append(node)

            while q:
                node = q.popleft()
                for nei in range(n):
                    if isConnected[node][nei] and nei not in seen:
                        seen.add(nei)
                        q.append(nei)

        for node in range(n):
            if node not in seen:
                provinces += 1
                bfs(node, isConnected, seen)
        return provinces




