class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {boolean}
     */
    containsNearbyDuplicate(nums: number[], k: number): boolean {
        const winSet:Set<number> = new Set();
        for(let r = 0; r<nums.length; r++){
            if(r>k) winSet.delete(nums[r-k -1]);
            if(winSet.has(nums[r])) return true;
            winSet.add(nums[r]);
        }
        return false;
    }
}
