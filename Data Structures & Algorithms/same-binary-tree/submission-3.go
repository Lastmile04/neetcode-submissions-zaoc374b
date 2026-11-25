func isSameTree(p *TreeNode, q *TreeNode) bool {
    queue1 := []*TreeNode{p}
	queue2 := []*TreeNode{q}

	for len(queue1) >0 && len(queue2) > 0{
		c1 := queue1[0]
		c2 := queue2[0]

		queue1 = queue1[1:]
		queue2 = queue2[1:]

		if c1 == nil && c2 == nil{
			continue
		}

		if c1 == nil || c2 == nil{
			return false
		}

		if c1.Val != c2.Val{
			return false
		}

		queue1 = append(queue1, c1.Left, c1.Right)
		queue2 = append(queue2, c2.Left, c2.Right)
	}
	return len(queue1) == len(queue2)
}
