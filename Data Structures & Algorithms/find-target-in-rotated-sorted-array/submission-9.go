func search(nums []int, target int) int {
	l,r:=0,len(nums)-1
	for l<=r{
		mid:= l + (r-l)/2

		// match mid
		if nums[mid] == target{
			return mid
		}
		// check if first half is sorted
		if nums[l] <= nums[mid]{
			if nums[l] <= target && target <= nums[mid]{
				r = mid-1
			}else{
				l = mid+1
			}
		}else{
			// otherwise the other half is sorted
			if nums[mid] <= target && target <= nums[r]{
				l = mid+1
			}else{
				r = mid-1
			}
		}
	}
	return -1
}
