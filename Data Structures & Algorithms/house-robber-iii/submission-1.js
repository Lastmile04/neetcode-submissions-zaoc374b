/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    /**
     * @param {TreeNode} root
     * @return {number}
     */
    rob(root) {
        // #return pair[with root, without root]
        const dfs = (node)=>{
            if(!node) return [0,0];

            const leftPair = dfs(node.left);
            const rightPair = dfs(node.right);

            return [node.val+leftPair[1]+rightPair[1], Math.max(...leftPair)+Math.max(...rightPair)];
        };

        const result = dfs(root);
        return Math.max(...result);

    }
}
