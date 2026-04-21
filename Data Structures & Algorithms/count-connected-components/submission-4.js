/*
 * How am i supposed to figure out this problem?
 * -> First lets try a DFS approch simple traverse the adjacency list/graph 
 *  -> For a second and more appropriat approah i will try the union find approach after reviewing how to do it as it seems like i have forgotton 
 *
 *
 * DFS:
 * Since in a connected component each node can be visited through any other node.
 * to find new connected component we can simply check if we're starting dfs from an unvisited node 
 *
 * */
class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        // initiate an empty adjacency list 
        const adjList = Array.from({length:n}, ()=>[]);
        // create a visited array
        const visited = Array(n).fill(false);

        // build the adjacency list 
        for(const[u,v] of edges){
            adjList[u].push(v);
            adjList[v].push(u);
        }

        const dfs = (node)=>{
            
            for(const nei of adjList[node]){
                if(!visited[nei]){
                    visited[nei] = true;
                    dfs(nei);
                }
            }
        };

            let res = 0;
            for(let node = 0; node < n; node++){
                if(!visited[node]){
                    visited[node] = true;
                    dfs(node);
                    res++;
                }
            }
        return res;
    }
}
