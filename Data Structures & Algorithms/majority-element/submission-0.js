class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    majorityElement(nums) {
        let candidate = 0,
        count = 0;

        for( let n of nums){
            if(count === 0) candidate = n;
            count += n === candidate ? 1 : -1;
        }
        
        return candidate
        
    }
}