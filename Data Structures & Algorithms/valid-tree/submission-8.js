class DSU {
    constructor(n) {
        this.parent = Array.from({ length: n }, (_, i) => i);
        this.rank = Array(n).fill(1);
    }

    find(node) {
        if (this.parent[node] !== node) this.parent[node] = this.find(this.parent[node]);
        return this.parent[node];
    }

    union(x, y) {
        let rootX = this.find(x),
            rootY = this.find(y);

        if (rootX === rootY) return false;
        if (this.rank[rootX] > this.rank[rootY]) this.parent[rootY] = rootX;
        else if (this.rank[rootX] < this.rank[rootY]) this.parent[rootX] = rootY;
        else {
            this.parent[rootY] = rootX;
            this.rank[rootX]++;
        }
        return true;
    }
}

class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        if (edges.length !== n - 1) return false;

        const dsu = new DSU(n);
        for (const [u, v] of edges) {
            if (!dsu.union(u, v)) return false;
        }
        return true;
    }
}
