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
First I will try the bfs approach using the khan's algo
1. create an empty indegree list
'''

# time complexity


# space complexity


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []

        # create the indegree shell list
        indegree = [0] * numCourses

        # create the empty adjacency list
        graph = [[] for _ in range(numCourses)]

        # fill the indegree and adjacency list
        for a,b in prerequisites:
            indegree[a] +=1
            graph[b].append(a)
        
        # initialize and fill queue
        q = deque()
        
        for n in range(numCourses):
            if indegree[n] == 0:
                order.append(n)
                q.append(n)

        # process each node
        while q:
            node = q.popleft()
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    order.append(nei)
                    q.append(nei)
        
        if len(order) == numCourses:
            return order
        else:
            return []



