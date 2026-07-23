func minimumDifference(nums []int, k int) int {
	if len(nums) < 2 || k < 2{
		return 0
	}
	sort.Ints(nums)
	m := math.MaxInt64

	for i:= k-1; i< len(nums); i++{
		m = min(m, nums[i] - nums[(i-k)+1])
	}
	return m
}