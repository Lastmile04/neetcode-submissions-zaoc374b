func maxSlidingWindow(nums []int, k int) []int {
    var res []int
	var queue []int
	for r:=0;r<len(nums);r++{
		for len(queue) > 0 && nums[queue[len(queue)-1]] <= nums[r]{
			queue = queue[:len(queue)-1]
		}

		queue = append(queue,r)

		if queue[0] <= r-k{
			queue = queue[1:]
		}

		if r>=k-1{
			res = append(res, nums[queue[0]])
		}
	}
	return res
}
