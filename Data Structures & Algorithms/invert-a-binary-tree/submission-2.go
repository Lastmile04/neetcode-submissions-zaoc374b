/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func invertTree(root *TreeNode) *TreeNode {
    if root == nil{
		return nil
	} 

	queue := []*TreeNode{root}

	for len(queue) > 0{
		current := queue[0]
		queue = queue[1:]
		current.Left, current.Right = current.Right, current.Left

		if current.Left != nil{
			queue = append(queue, current.Left)
		}
		if current.Right != nil{
			queue = append(queue, current.Right)
		}
	}
	return root
}
