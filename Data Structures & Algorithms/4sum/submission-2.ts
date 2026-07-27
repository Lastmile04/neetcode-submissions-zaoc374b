class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[][]}
     */
    fourSum(nums: number[], target: number): number[][] {
        const result: number[][] = [];
        const n = nums.length;

        if (n < 4) return result;
        nums.sort((a, b) => a - b);

        for (let i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] === nums[i - 1]) continue;
            if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break;
            if (nums[i] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target) continue;

            for (let j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] === nums[j - 1]) continue;
                if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) break;
                if (nums[i] + nums[j] + nums[n - 2] + nums[n - 1] < target) continue;

                let l = j + 1;
                let r = n - 1;

                while (l < r) {
                    const sum = nums[i] + nums[j] + nums[l] + nums[r];

                    if (sum === target) {
                        result.push([nums[i], nums[j], nums[l], nums[r]]);

                        while (l < r && nums[l] === nums[l + 1]) l++;
                        while (l < r && nums[r] === nums[r - 1]) r--;

                        l++;
                        r--;
                    } else if (sum < target) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
        }
        return result;
    }
}
