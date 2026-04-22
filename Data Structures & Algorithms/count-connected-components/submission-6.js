class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {number}
     */
    countComponents(n, edges) {
        const par = Array.from({ length: n }, (_, i) => i);
        const rank = Array(n).fill(1);


        function find(x) {
            if (x !== par[x]) par[x] = find(par[x]);
            return par[x];
        }

        function union(x, y) {
            let rootX = find(x),
                rootY = find(y);

            if (rootY === rootX) return false;

            if (rank[rootY] > rank[rootX]) par[rootX] = rootY;
            else if (rank[rootY] < rank[rootX]) par[rootY] = rootX;
            else {
                par[rootY] = rootX;
                rank[rootX] += 1;
            }
            return true;
        }

        let res = n;
        for (const [u, v] of edges) {
            res -= union(u, v);
        }
        return res;
    }
}
