/*
 * Steps for this problem :
 * 1-> Initiate a queue whith root in it
 * 2-> while loop
 * 3-> array for elements in each level 
 * 4-> for loop
 * 5-> pop each element and push into lvl use q.shift()
 * 6-> push children of each element into queue
 * */

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
     * @return {number[][]}
     */
    levelOrder(root) {
        const res = [];
        if(!root) return res;

        let q = [root];
        while(q.length > 0){
            const lvl = [];
            const length = q.length;
            for(let i = 0; i < length; i++){
                const node = q.shift();
                lvl.push(node.val);
                if(node.left) q.push(node.left);  
                if(node.right) q.push(node.right);
            }
            if (lvl.length > 0) res.push(lvl);
        }
        return res;
    }
}

