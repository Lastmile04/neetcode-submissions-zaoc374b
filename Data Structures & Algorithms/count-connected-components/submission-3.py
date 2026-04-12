# Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->
'''
Quite a simple problem, that we can solve using either dfs/bfs or union find method, i will try the union find method only since it's the most intuitive solution 
even though the bfs/dfs solution is not bad at all and is intuitive in itself by using a visited set to keep track of the visited nodes and then use that to 
eventually keep track of the connected components. 
the time complexity of this might be O(e+v)

Now union find which is like made for a problem like this.
'''

# Approach
'''
- maintain two arrays:
- Parent array -> at start is each node is the parent of itself {index = node, value on that index = parent, so initially each node is a parent itself}
- as we go through each edge what we're gonna do is like this for a edge [0,1] 0 is the parent itself but now 1's parent is also 0 {0<-1}
- now that we've made a connection how can we track the numbher of connected componentsl, for that since at start we can say each node is a connected component
but we start making connection based on edges, we can keep decrementing the number of connected components till we eventually end up with the solution
- always add to the root node 
- to make connection is pretty simple simply check the root node of both the nodes, like [0,1], [1,2] here initially each node was it's own parent then connections
were built making 0 parent of itself and 1 now if 2 was connected to 1 already then we'll say since 2 to connected to 1 and 1 to 0 making 0 both there's root node
there's no need for connection but now 2 is a parent of itself and according to edges [1,2] meaning 2 is connected to 1 so we directly connect 2 to the root node of 1
which is 0, the proper connection is made based on the size of the node/component since 0 has size 2 and 2 has size 1, 0 becomes the parent being the bigger component

OPTIMZATION:
- A subtle easy optimization for this problem is maintaing a size which basically means that for every single node we're gonnna maintain what's the size of it
-  so how this size optimization works is that, initially we create a size array giving every single componenet a size of one and as we perform union based on the
edges some componets starts merging and losing their status as parent which keeps there size at 1 but like the earlier example of edge[0,1] when 0 becomes 1's parent
it's size jumps form 1 to 2. { basicallly meaning what's the size of this node if it's the parent }
- how this concept works is that size determines which connection is better to make should a size 2 componenet become a child of size 1 or vice versa.

Operations:
FIND: use to find the root/parent of a node
UNION: detects cycle and uses size to perform union or merge components  
'''
# time complexity
# 

# space complexity
# 


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        size = [1] * n

        # find operation
        def find(x):
            if par[x] != x:
                # path compression basically by setting the current node's parent to it's grand parent if it exists, simply skipping checking the parent itself
                # two ways to do it 1 is somewhat manual other is simply recursion
                # par[x] = par[par[x]]
                par[x] = find(par[x])
            return par[x]
        
        # union operation
        # this is union by size
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return 0

            if size[rootX] > size[rootY]:
                par[rootY] = rootX
                size[rootX] += size[rootY]

            elif size[rootX] < size[rootY]:
                par[rootX] = rootY
                size[rootY] += size[rootX]
            else:
                par[rootY] = rootX
                size[rootX] += size[rootY]
            return 1 
        
        res = n
        for e, v in edges:
            # if a union is made the resulting connected componects gets decremented leading to a correct solution
            res -= union(e, v)
        return res