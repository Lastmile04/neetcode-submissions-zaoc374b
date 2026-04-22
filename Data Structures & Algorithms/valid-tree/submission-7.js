
class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
    */
    validTree(n, edges) {
        if (edges.length > n - 1) return false;

        const adj = Array.from({ length: n }, () => []);
        const visit = new Set();

        for (const [u, v] of edges) {
            adj[u].push(v);
            adj[v].push(u);
        }

        let q = [[0, -1]];
        visit.add(0);

        let i = 0;
        while (i < q.length) {
            let node = q[i++];
            let [curr, par] = node;

            for (const nei of adj[curr]) {

                if (nei === par) continue;
                if (visit.has(nei)) return false;

                visit.add(nei);
                q.push([nei, curr]);

            }
        }
        return visit.size === n;
    }
}
