class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        const numSet = new Set(nums);
        let res = 0;

        for(let num of numSet){
            if(!numSet.has(num-1)){
                let len = 1;
                while(numSet.has(num+len)){
                    len++;
                }
                res = Math.max(res, len);
            }
        }
        return res;
    }
}
