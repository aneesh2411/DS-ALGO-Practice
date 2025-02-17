# We will be given an edge list, which is a list of tuples, where each tuple represents an edge between two nodes.
# We will be given a start node and a target node.
# Example:
# edge_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)]

# We will use an adjacency list to represent the graph.
from collections import defaultdict
edge_list = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 1)]

#Graphical representation of the edge list:
# 1 - 2
# 2 - 3
# 3 - 4
# 4 - 5
# 5 - 6
# 6 - 7
# 7 - 8
# 8 - 9
# 9 - 10
# 10 - 1

D = defaultdict(list)
for u, v in edge_list:
    D[u].append(v)

    #if Undirected graph, we need to add both (u, v) and (v, u) to the adjacency list.
    D[v].append(u)

print(D) #Ad

#traversal techniques:
# We can use a queue to perform a BFS traversal.
print("BFS traversal using queue:")
from collections import deque
source = 1
seen = set()
q =deque()
q.append(source)
seen.add(source)
while q:
    node = q.popleft()
    print(node)
    for nei in D[node]:
        if nei not in seen:
            seen.add(nei)
            q.append(nei)

# We can use a stack to perform a DFS traversal.
#clear the seen set
seen.clear()

stack = [source]
print("DFS traversal using stack:")
while stack:
    node = stack.pop()
    print(node)
    for nei in D[node]:
        if nei not in seen:
            seen.add(nei)
            stack.append(nei)

# We can also traverse the graph using recursion.
#clear the seen set
seen.clear()
print("DFS traversal using recursion:")
def dfs(node):
    print(node)
    for nei in D[node]:
        if nei not in seen:
            seen.add(nei)
            dfs(nei)

dfs(source)
# We will use a set to keep track of visited nodes. Example: visited = set()

# We will use a dictionary to keep track of the parent of each node.
# We will use a dictionary to keep track of the distance of each node from the start node.
