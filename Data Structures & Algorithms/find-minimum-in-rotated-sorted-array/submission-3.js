class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let l = 0,
            r = nums.length-1;
        let res = nums[0];

        while(l<=r){
            if(nums[l] < nums[r]){
                res = Math.min(res, nums[l]);
                break;
            }

            const mid = l + Math.floor((r-l)/2);
            res = Math.min(res, nums[mid]);

            // check if sorted 
            if(nums[l] <= nums[mid]) l = mid + 1;
            else r = mid;
        }
        return res;
    }
}
