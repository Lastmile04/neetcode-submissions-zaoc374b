class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {boolean}
     */
    search(nums, target) {
        let l = 0,
            r = nums.length-1;
        while(l<=r){
            const mid = Math.floor(l+(r-l) / 2);
            if(nums[mid] === target) return true
            // check if left is sorted
            if(nums[l] < nums[mid]){
                // check if target is b/w left portion
                if( nums[l] <= target && target < nums[mid] ){
                    r = mid-1;
                }
                else{
                    l=mid+1;
                }
            }
            // check if right is sorted
            else if(nums[l] > nums[mid]){
                if(nums[mid] < target && target <= nums[r]){
                    l = mid+1;
                }
                else{
                    r = mid-1;
                }
            }
            else{
                l++;
            } 
        }

        return false;
    }
}
