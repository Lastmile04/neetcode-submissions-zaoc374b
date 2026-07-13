class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums: number[], k: number): boolean {
        const map = new Map();

        for(let r = 0; r<nums.length; r++){
            if(map.has(nums[r]) && r - map.get(nums[r]) <= k ) return true;
            map.set(nums[r], r)
        }
        
        return false
    }
}
