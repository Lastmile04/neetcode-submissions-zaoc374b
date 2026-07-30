class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums: number[]): number {
        let s =0;
        let count = 1;
        for( let f = 1; f<nums.length; f++){
            if(nums[f] === nums[f-1])count++; 
            if ( nums[f] === nums[f-1] && nums[f] === nums[f-2] && count > 2) continue;
            if(nums[f] !== nums[f-1]) count = 1;
            s++;
            nums[s] = nums[f];
        }
        return s+1;
    }
}