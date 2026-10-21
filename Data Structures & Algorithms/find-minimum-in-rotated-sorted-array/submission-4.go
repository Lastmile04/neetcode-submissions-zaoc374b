func findMin(nums []int) int {
	if len(nums)==1{
		return nums[0]
	}

	if len(nums) == 2{
		if nums[0] < nums[1]{
			return nums[0]
		}else{
			return nums[1]
		}
	}

	l:=0
	r:= len(nums)-1
	for r-l+1 != 2{
		mid := l + (r-l)/2
		if nums[mid]>nums[r]{
			l = mid
		}else{
			r = mid
		}
	}
	if nums[l] > nums[r]{
		return nums[r]
	}else{
		return nums[l]
	}

}
