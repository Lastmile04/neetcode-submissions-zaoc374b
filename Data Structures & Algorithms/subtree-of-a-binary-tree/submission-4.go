func isSubtree(root *TreeNode, subRoot *TreeNode) bool {
	if subRoot == nil {
		return true
	}
	if root == nil {
		return false
	}

	// Check if the trees match starting at the current node
	if isSameTree(root, subRoot) {
		return true
	}

	// Otherwise, keep searching in the left and right subtrees
	return isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	// Both are nil: structurally identical at this branch
	if p == nil && q == nil {
		return true
	}
	// Only one is nil, or values don't match
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
