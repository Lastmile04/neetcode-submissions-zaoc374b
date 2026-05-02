class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const res = Array.from({length: nums.length}, (_, i)=> (1));

        let prefix = 1;
        let suffix = 1; 

        for(let i = 0; i<nums.length; i++){
            res[i] = prefix;
            prefix = prefix * nums[i];
        }

        for(let i = nums.length-1; i >=0 ; i--){
            res[i] = suffix * res[i];
            suffix = suffix * nums[i];
        }
        return res;

    }
}
