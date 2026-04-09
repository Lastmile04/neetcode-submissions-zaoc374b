# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
'''
The problem is similar to the previous problem of course schedule, after analyzing the problem statement and some given examples, I realized the way to order is 
simply like how in the previous problem during the bfs solution I used the khan's algo to calculate indegree and use that indegree list to check if there's a cycle
I can use the same concept from khan's algo of taking the ones with no prerequisite first and order them in that way, while also returing empty list if a cycle is
found.
'''


# Approach
'''
BFS:
First I will try the bfs approach using the khan's algo
1. create an empty indegree list and an empty adjacency list based on the number of edges
2. fill both the lists
3. fill the queue with indegree 0 nodes and fill the order list
4. process each and fill the order list based on the updates indegree
'''

'''
DFS:
For the dfs approch I will try
1. create an adjacency list first
2. 3 states-> visiting(in the recursive stack) 1, visited 2 and unvisited 0
3. Do the normal dfs cycle detection procedure, just after a node is visited append it to the final list
IMP: since we do pre-order traversal the final order list to return must be reversed first
'''

# time complexity
# O(V+E)

# space complexity
# O(V+E)

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        # create the empty adjacency list
        graph = [[] for _ in range(numCourses)]

        # fill the adjacenecy list
        for a,b in prerequisites:
            graph[b].append(a)
        
        # build a state list
        state = [0] * numCourses
        
        def dfs(node):
            # base cases
            # visiting
            if state[node] == 1:
                return False

            # visited
            if state[node] == 2:
                return True

            # change the state to visiting
            state[node] = 1

            # loop and visit neighbours
            for nei in graph[node]:
                if not dfs(nei): return False
            # mark as visited
            state[node] = 2
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return order[::-1]
