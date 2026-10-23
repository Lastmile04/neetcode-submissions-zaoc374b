func topKFrequent(nums []int, k int) []int {
	if len(nums) == 1{
		return nums
	}

	freq := make(map[int]int)

	for _, num:= range nums{
		freq[num]++
	}

	buckets := make([][]int, len(nums)+1)
	for n,f := range freq{
		buckets[f] = append(buckets[f], n)
	}

	var res []int
	for i:= len(buckets) - 1; i>=0; i--{
		res= append(res, buckets[i]...)

		if len(res) >= k{
			return res[:k]
		}
	}
	return res
}
