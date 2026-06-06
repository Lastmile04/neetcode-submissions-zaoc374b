class Solution {
    /**
     * @param {number} a
     * @param {number} b
     * @param {number} c
     * @return {string}
     */
    longestDiverseString(a, b, c) {
        const res = [];

        const canUse = (ch)=>{
            const n = res.length;

            return !(
                n>=2 &&
                res[n-1] === ch &&
                res[n-2] === ch
            );
        };

        while(true){
            const chars = [
                [a, 'a'],
                [b, 'b'],
                [c, 'c']
            ];

            chars.sort((x, y)=> y[0] - x[0]);
            let placed = false;
            
            for( const[count, ch] of chars){
                if(count === 0 ) continue;
                if(!canUse(ch))continue;

                res.push(ch);
                
                if(ch === 'a') a--;
                else if(ch === 'b') b--;
                else c--;

                placed = true;
                break;
            }
            if(!placed) break;
        }
        return res.join('');
    }
}
