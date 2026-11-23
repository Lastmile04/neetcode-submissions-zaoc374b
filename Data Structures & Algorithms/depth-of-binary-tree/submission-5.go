/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func maxDepth(root *TreeNode) int {
	if root == nil{
		return 0
	}
   	queue := []*TreeNode{root}
   	depth := 0

   	for len(queue) > 0{
		level := len(queue)
		for i:=0; i<level; i++{ 
		node := queue[0]
		queue = queue[1:]
		if node.Left != nil{
			queue = append(queue, node.Left)
		}
		if node.Right != nil{
			queue = append(queue, node.Right)
		}
		}
		depth++
   }
   return depth

}
