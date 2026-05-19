class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @return {number[]}
     */
    findMinHeightTrees(n, edges) {
        if(n === 1) return [0];
        const degree = Array(n).fill(0);
        const adjList = Array.from({ length: n }, ()=>[]);
        const leaves = [];
        let front = 0;
        // fill the adjList 
        for(const [n1, n2] of edges){
            adjList[n1].push(n2);
            adjList[n2].push(n1);
        }

        
        
        for(let i = 0; i < n; i++){
            // fill the degree list 
            degree[i] = adjList[i].length;
            // fill the leaves {nodes with only 1 degree} to the queue for bfs
            if(adjList[i].length === 1) leaves.push(i);
        }

        // perform bfs
        while(front < leaves.length){
            if (n <= 2) return leaves.slice(front);

            const size = leaves.length - front;
            for(let i = 0; i < size; i++){
                // pop the value
                const val = leaves[front++];
                n--;
                for(const nei of adjList[val]){
                    degree[nei]--;
                     if(degree[nei] === 1){
                        leaves.push(nei);
                     }
                }
            }

        }

        return [];

    }
}
