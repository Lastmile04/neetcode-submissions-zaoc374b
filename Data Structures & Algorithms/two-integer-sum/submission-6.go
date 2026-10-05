func twoSum(nums []int, target int) []int {
	sumMap := make(map[int]int)
    for i, num:= range nums{
		complement := target - num
		if j, ok := sumMap[complement]; ok{
			return []int {j,i}
		}
		sumMap[num] = i
	}
	return nil
}
