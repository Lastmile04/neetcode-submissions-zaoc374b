// start a sliding window shrink window if the element is already seen and remove the elemets from set 
class Solution {
    /**
     * @param {string} s
     * @return {number}
     */
    lengthOfLongestSubstring(s) {
        // // set of seen elements
        // let seen = new Set();

        let map = new Map()
        let res = 0;

        // initialize window
        let l = 0;

        for( let r = 0; r < s.length; r++ ){

        //     while( seen.has(s[r]) ){
        //         seen.delete(s[l])
        //         l+=1
        //     }
        //     seen.add(s[r])
        //     res = Math.max(res, r-l+1)

            if (map.has(s[r])){
                l = Math.max(l, map.get(s[r]) + 1);
            }

            map.set(s[r], r)
            res = Math.max(res, r-l+1)
        }
        return res
    }
}
