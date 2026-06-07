class Solution {
    /**
     * @param {number[][]} triplets
     * @param {number[]} target
     * @return {boolean}
     */
    mergeTriplets(triplets, target) {
        let x = 0,
            y = 0,
            z = 0;

        for(const [a, b, c] of triplets){
            if(
                a <= target[0] &&
                b <= target[1] &&
                c <= target[2]
            )
            {
                x = Math.max(x, a);
                y = Math.max(y, b);
                z = Math.max(z, c);
            }
        }

        if(
            target[0] === x &&
            target[1] === y &&
            target[2] === z
        ){
            return true;
        }
        else return false;

    }
}
