# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
'''
What i can initially see in this problem is that it's similar to the previous ones, we have data we create an adjacency list to simulate a graph, and then finally
check if that graph has any cycles and if all the nodes in the graph are connected. 

that's what i thought initially but the reality was different it's not similar to the previous problem it has some elements like visited set and parent tracking
unique to it.

For a valid graph, two things must be true in a graph:
- everything is connected 
- no cycles
'''


# Approach
'''

- build graph
- traverse from node 0
- track visited
- detect cycle 
- checck if all nodes visited
'''

'''
DFS:
the approach is to have the current node and the parent of said node, and if neighbour is visited and neighbour is not parent of the current node then it's a cycle
so two things to monitor is:
- visited set 
- parent tracking

in neighours:
- if a neighbour is parent then skip
- if it's already visited then return False

in the dfs approach we use dfs only for cycle detection and to fill up the visited array through traversal
the end check is still to make sure that graph might not have any cycles but if any node is separate form the rest of the graph will still make the graph unvalid
'''

'''
BFS:
- do the edges check
- create adjacency list and fill it
- initialize a visited set and put the first node in it as visited
- initiate queue with the first node (node, parent) {take parent as -1 for the first node}
- process the node in the queue
- traverse the neighboursL:
    - if parent then skip
    - if visited then False
    - mark the current neighbour as visited 
    - push the current neighbour and it's parent node into the queue for further processing
'''

'''
Dijoint Set Union:
- node starts in it's own componenets 
- when we connect two nodes:
    - if they are already in the same component, adding this edge creates a cycle
    - otherwise the componenets are merged
- a vaild tree must have exactly one connected component
'''
# time complexity
# O(V+E)

# space complexity
# O(V+E)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False
        
        parent = [i for i in range(n)]
        rank = [1] * n  # optional optimization

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            # cycle detected
            if rootX == rootY:
                return False

            # union by rank (optional but good practice)
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX] += 1

            return True

        for u, v in edges:
            if not union(u, v):
                return False

        return True


                




