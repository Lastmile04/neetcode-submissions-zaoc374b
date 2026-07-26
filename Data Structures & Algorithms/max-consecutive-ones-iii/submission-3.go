func longestOnes(nums []int, k int) int {
   var maxcount, l, replace int
   for r, rval := range(nums){
	   if rval == 0 {
		   replace++
	   }
	   for replace > k{
		   if nums[l] == 0 {
			   replace--
		   }
           l++
	   }
	   maxcount = max(maxcount, r-l+1)
   }
   return maxcount
}
