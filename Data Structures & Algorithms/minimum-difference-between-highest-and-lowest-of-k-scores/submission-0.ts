class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    minimumDifference(nums: number[], k: number): number {
        nums.sort((a,b)=> a-b);
        let l = 0,
            min = Infinity;
        
        for(let r = 0; r<nums.length; r++){
            if(r-l+1 === k){
                const currMin = nums[r] - nums[l];
                min = Math.min(min, currMin);
                l++;
            }
        }
        return min;
    }
}