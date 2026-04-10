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

'''

# time complexity


# space complexity

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set([0])
        q = deque([(0,-1)])

        while q:
            node, parent = q.popleft()

            for nei in graph[node]:
                if nei == parent:
                    continue

                if nei in visited:
                    return False
               
                if nei not in visited:               
                    visited.add(nei)
                    q.append((nei, node))

        return len(visited) == n

                




