class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let map = new Map()
        for (let value of nums){
            if ( map.has(value) ) return true
            else map.set(value)
        }
        return false
    }
}
