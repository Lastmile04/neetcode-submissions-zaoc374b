class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {void} Do not return anything, modify nums in-place instead.
     */
    reverse(nums, l, r) {
        while (l < r) {
            [nums[l], nums[r]] = [nums[r], nums[l]];
            l++;
            r--;
        }
    }

    rotate(nums, k) {
        k = k % nums.length;
        if(k===0) return;

        this.reverse(nums, 0, nums.length-1);
        this.reverse(nums, 0, k-1);
        this.reverse(nums, k, nums.length-1);
    }
}
