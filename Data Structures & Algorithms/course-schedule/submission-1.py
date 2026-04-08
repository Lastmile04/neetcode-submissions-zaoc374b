# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
# a list of prerequisites, the integer that comes after should be taken first than the integer that comes before it, the courses are from 0 to n-1, simply have to
# return true or false based on if all the courses can be completed or not
# more importantly each element in the numCourses array is an array itself, making numCourses an array of array
# so for each element we have to check if the current orientation of courses is possible to accomplish or not
# each element inside the array can only have 2 elements themselves but the value of the elements inside the element can be 0-n


# Approach
# so what should the approach be, based on the examples given the first one being a single element meaninig a single array so that automatically true since the
# the courses can only be 0 or 1 and 1 element ensures both can be accomplished 
# but the second example has [0, 1] and then [1, 0] when on the first element based on the prerequisite rule 1 must be taken first and then 0, which is fine but when
# the second element comes the order reverses, since previously to take 0 we had to take 1 now, to take 1 we have to take 0 which is impossible 
# this leads to some different possibilities like what if, some courses are interdependented accross elements, for eg, what if [1, 0] [2, 0] : now in this scenario
# to take one we have to take 0 but to take 0 we have to take 2 and it's possible since they don't contradict 
# both dfs and bfs can work on this probelem

# first i'll try the dfs approach:
# since this is a graph problem we have to think in terms of a graph, each course is a node which give 2 nodes a & b and this makes it a directed graph where
# b -> a and this also makes much more sense when we see the failed case from this prespective, in the failed case 0->1->0 making it a cycle in a directed graph
# we have to create a directed graph as an adjacency list and then detect if that graph has any cycles in it
#  An adjacency list is a mapping of nodes to lists, used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
# For simplicity, nodes values are numbered from 1 to n, where n is the total number of nodes in the graph. The index of each node within the adjacency list
# is the same as the node's value (1-indexed).
# for dfs approach we need to monitor 3 states, since we need to do cycle detection, visited, visiting and not visited, so when doing dfs, if we go to a node that 
# is already visiting we found a cycle
# 0 for unvisited, 1 for visiting( in recursive stack ) and 2  for (fully done) 
# create a state list to monitor state of each node

# in dfs:
# base case is cycle detected and return false using state list 
# mark the state as visiting using state list as node is just an index and not actually created using a class
# explore the neighbours 
# the only reason to return true along with false is so that it does not cause any problems with python behaviour

### key point if it is not stated that it's true python assumes it None instead of the other logical assumption of flase and vice versa

# the bfs approach
# basically we use the khan's algo to find out if the graph can be topologicaly sorted or not, if it can be sorted then that means the graph is acyclic if not 
# that means a cycle is present.

# in khan's algo the concept of indegree is used meaning for each course how many prerequisites does it have 
# start with courses that have no prerequisites, these are the only ones that can be taken immediately
# so build an indegree array 
# 

# time complexity

# space complexity

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # build indegree array
        indegree = [0] * numCourses

        # create an empty adjacency list for directed graph
        graph = [[] for _ in range(numCourses)]
        for a,b in prerequisites:
            indegree[a] +=1
            graph[b].append(a)
        
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
            
        finish = 0
        while q:
            node = q.popleft()
            finish+=1
            for nei in graph[node]:
                indegree[nei] -=1
                if indegree[nei] == 0:
                    q.append(nei)
        return finish == numCourses