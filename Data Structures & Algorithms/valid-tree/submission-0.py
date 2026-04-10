# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
'''
What i can initially see in this problem is that it's similar to the previous ones, we have data we create an adjacency list to simulate a graph, and then finally
check if that graph has any cycles and if all the nodes in the graph are connected.

For a valid graph, two things must be true in a graph:
- everything is connected 
- no cycles
'''


# Approach
'''
similar approach for both dfs(states marking) and bfs(khan's algo)
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
'''

# time complexity


# space complexity

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        visited = set()
        graph = [[] for _ in range(n)]

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node, parent):

            if node not in visited:
                visited.add(node)

            for nei in graph[node]:
                if nei == parent: 
                    continue
                
                if nei in visited: 
                    return False
                
                # traverse
                if not dfs(nei, node):
                    return False
            
            return True
        
        if not dfs(0, -1):
            return False

        return len(visited) == n