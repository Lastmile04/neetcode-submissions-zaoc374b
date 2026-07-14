func containsNearbyDuplicate(nums []int, k int) bool {
	helpMap := make(map[int]bool)
	L := 0
	for R, num := range nums{
		if R-L > k {
			delete(helpMap, nums[L])
			L++
		}
		if helpMap[num] {
			return true
		}

		helpMap[num] = true
	}
	return false
}
