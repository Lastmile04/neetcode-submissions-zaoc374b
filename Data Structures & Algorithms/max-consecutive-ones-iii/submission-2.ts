class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number}
     */
    longestOnes(nums: number[], k: number): number {
        let maxCount = 0,
            l = 0,
            replace = 0;
        for(let r = 0; r<nums.length; r++){
            if(nums[r] === 0) replace++;
            while(replace > k){
                if(nums[l] === 0) replace--;
                l++
            }
            maxCount = Math.max(maxCount, r-l+1);
        }
        return maxCount;
    }
}
