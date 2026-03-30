class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let set  = new Set()
        for (let value of nums){
            if ( set.has(value) ) return true
            else set.add(value)
        }
        return false
    }
}
