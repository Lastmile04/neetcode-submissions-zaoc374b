class Solution {
    /**
     * @param {string} s1
     * @param {string} s2
     * @return {boolean}
     */
    checkInclusion(s1, s2) {

        if(s1.length > s2.length) return false;

        const freqMapS1 = new Map(); 
        for(const ch of s1){
            freqMapS1.set(ch, (freqMapS1.get(ch) || 0) +1); 
        }

        const freqMapWin = new Map();
        let l = 0;

        for(let r = 0; r < s2.length; r++){
            freqMapWin.set(s2[r], (freqMapWin.get(s2[r]) || 0) + 1);

            if(r-l+1 > s1.length){
                const charL = s2[l];
                if( freqMapWin.get(charL) === 1) freqMapWin.delete(charL);
                else freqMapWin.set(charL, freqMapWin.get(charL) - 1);
                l++;
            }

            if( r-l+1 === s1.length){ 
                if(this.isMatch(freqMapS1, freqMapWin)) return true; 

            }

        }
        return false;
    }

    isMatch(map1, map2){
        if(map1.size !== map2.size) return false;

        for(let [key,val] of map1){
            if(map2.get(key) !== val) return false;
        }
        return true;
    }
}

