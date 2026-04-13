'''
<-Initial views of this probelm-->
- First I'll try the union find approch since on paper dry run was able to find the correct edge, this is basically finding a cycle
if nodes with same parents are found that means a cycle is there, which tells us which edge to remove
since there can be multiple edges that can be removed to get the desired outcome i am thinking of having an edge array which will update with the latest 
edge to return the one that appear last in edges array
'''
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent = [i for i in range(n)]
        rank = [1] * n
        edge = []
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            
            if rootX == rootY:
                return False
                
            
            if rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            elif rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            else:
                parent[rootY] = rootX
                rank[rootX]+=1

            return True

        # update edge each time a new cycle is found
        for u, v in edges:
            if not union(u,v):
                edge = [u,v]
        
        return edge

            