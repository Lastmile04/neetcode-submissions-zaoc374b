"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# Approach
# at first this seems like a simple traversal problem but then the problem of this being a graph and not a tree comes up meaining this can be cyclic,
#  so have to think of a way to prevent deduplication of nodes to prevent infinite loops while traversing
# the base plan still is to use dfs/bfs for traversing the negihbours and then returning the copy
# each index is the val of the node with the list on that index being it's neighbor
# Using hashset can be viable as we can maintain a set of seen nodes and check if the current node is already visited or not
# but i think it'll be much better to use a hashmap instead and just map the OG nodes to it's clone counterpart 
# HashMap is the better play here because I do not just need to keep track of the visited nodes i also need to construct the clones graph as it's not just traversal
# Hashset only give you a yes or no about "Have I Seen this node?", but it does not provide the where have i seen this node, for that we use hashMap
# since it tells us exactly "“Have I seen this node, and if yes, where is its clone?”"

# Complexity
# time
# bfs or dfs both will have O(V+E) since each element is visited once, and since we visit each vertex and there edge the time adds up
# space
# space is simply O(V) since the hasmap is the same size of original graph and dfs/bfs at worst case can grow to O(V)


# intiate the hashmap
# check if the current node already exists in hashmap and if it does return the cloned node
# create a new clone node 
# map that to the OG node in hashmap
# call dfs on the neighbour -> returns the clones neighbors
# append to clone.neighbors

# the difference for bfs is that in while writing code for dfs we have to think how in each iteration the the funtion will run from top to bottom
# but in bfs the only iteration happens in the loop created inside the funtion not the function itself is called multiple times so before the loop it's just the initial case
# not something that can re occur like in dfs

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OG_to_clone = {}

        if not node:
            return None

        # def dfs(node, OG_to_clone):
        #     if node in OG_to_clone:
        #         return OG_to_clone[node]
        
        #     clone = Node(node.val)
        #     OG_to_clone[node] = clone

        #     for n in node.neighbors:
        #             clone.neighbors.append(dfs(n , OG_to_clone))
            
        #     return clone
        
        def bfs(node, OG_to_clone):
            q = deque([(node)])
            clone = Node(node.val)
            OG_to_clone[node] = clone

            while q:
                curr = q.popleft()
                curr_clone = OG_to_clone[curr]
                for n in curr.neighbors:
                    if n not in OG_to_clone:
                        OG_to_clone[n] = Node(n.val)
                        q.append(n)
                    curr_clone.neighbors.append(OG_to_clone[n])
            return clone

        return bfs(node, OG_to_clone)      