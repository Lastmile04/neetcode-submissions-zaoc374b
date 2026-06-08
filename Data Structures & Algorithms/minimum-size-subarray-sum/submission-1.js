class Solution {
    /**
     * @param {number} target
     * @param {number[]} nums
     * @return {number}
     */
    minSubArrayLen(target, nums) {
        let l = 0,
            currSum = 0,
            len = 0,
            res = Infinity;

        for (let r = 0; r < nums.length; r++) {
            currSum += nums[r];
            if (currSum >= target) { 
                while (currSum >= target) {
                    len = r-l+1;
                    currSum -= nums[l];
                    l += 1;
                    res = Math.min(res, len);
                }
            } 
        }
        if(res === Infinity) return 0;
        return res;
    }
}
