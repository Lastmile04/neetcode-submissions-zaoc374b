import "slices"
func minimumDifference(nums []int, k int) int {
	slices.Sort(nums)
	globalMinDiff := nums[len(nums) - 1]
	l := 0
	for r, val := range(nums){
		if r-l+1 == k{
			currMinDiff:= val - nums[l]
			globalMinDiff = min(globalMinDiff, currMinDiff) 
			l++
		}
	}
	return globalMinDiff
}
