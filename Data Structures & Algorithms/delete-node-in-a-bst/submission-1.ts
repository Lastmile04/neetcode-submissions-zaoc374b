class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} key
     * @return {TreeNode | null}
     */
    deleteNode(root: TreeNode | null, key: number): TreeNode | null {
        if (!root) return null;

        // Navigate the tree
        if (key > root.val) {
            root.right = this.deleteNode(root.right, key);
        } else if (key < root.val) {
            root.left = this.deleteNode(root.left, key);
        } else {
            // Target Node Found!
            
            // Case 1: No left child (covers leaf node and single right child cases)
            if (!root.left) return root.right;
            
            // Case 2: No right child (covers single left child case)
            if (!root.right) return root.left;
        
            // Case 3: Both children exist
            // 1. Find the in-order successor (minimum node in right subtree)
            let successor = root.right;
            while (successor.left) {
                successor = successor.left;
            }
            
            // 2. Overwrite target node's value with successor's value
            root.val = successor.val;
            
            // 3. Delete the successor node from the right subtree
            root.right = this.deleteNode(root.right, successor.val);
        }
        return root;
    }
}