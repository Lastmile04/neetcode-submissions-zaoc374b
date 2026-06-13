class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s, k) {
        let l = 0,
            count = new Map(),
            res = 0,
            maxF = 0;
        
        for(let r = 0; r<s.length; r++){
            count.set(s[r], (count.get(s[r]) || 0) +1);
            maxF = Math.max(maxF, count.get(s[r]));

            // till window is invalid
            while((r-l+1) - maxF > k){
                count.set(s[l], count.get(s[l])-1);
                l++;
            }
            res = Math.max(res, r-l+1);
        }

        return res;
    }
}
