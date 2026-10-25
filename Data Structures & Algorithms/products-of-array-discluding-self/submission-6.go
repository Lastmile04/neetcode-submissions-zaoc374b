func productExceptSelf(nums []int) []int {
	n := len(nums)
    res := make([]int, n)
    prefix := make([]int, n)
    suffix := make([]int, n)

	prefixProduct := 1
	postfixProduct := 1

	for j := len(nums)-1; j >= 0; j--{
		suffix[j] = postfixProduct
		postfixProduct *= nums[j]
	}

	for i, _:= range nums{
		prefix[i] = prefixProduct
		prefixProduct *= nums[i]
		res[i] = prefix[i] * suffix[i]
	} 

	return res
}
