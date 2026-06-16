class Solution {
    /**
     * @param {string} senate
     * @return {string}
     */
    predictPartyVictory(senate) {
        const R = [];
        const D = [];
        let Rfront = 0,
            Dfront = 0,
            n = senate.length;

        for(let s=0; s<n; s++){
            if(senate[s] === "R"){
                R.push(s);
            }else D.push(s);
        }

        while(Rfront < R.length && Dfront < D.length){
            const r = R[Rfront];
            const d = D[Dfront];

            if(r < d){
                R.push(r+n);
                Rfront++;
                Dfront++;
            }
            else{
                D.push(d+n);
                Dfront++;
                Rfront++;
            }
        }

        return Rfront < R.length ? "Radiant" : "Dire";

    }
}
