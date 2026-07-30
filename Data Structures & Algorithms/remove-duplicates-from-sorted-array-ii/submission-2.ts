class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    removeDuplicates(nums: number[]): number {
        if (nums.length <= 2) return nums.length;

        let s = 2; // Positions 0 and 1 are always valid
    
        for (let f = 2; f < nums.length; f++) {
        // Only write if current number is different from the number 2 slots behind our write pointer
            if (nums[f] !== nums[s - 2]) {
                nums[s] = nums[f];
                s++;
            }
        }
    
        return s;
    }
}