class Solution {
    /**
     * @param {number[][]} triplets
     * @param {number[]} target
     * @return {boolean}
     */
    mergeTriplets(triplets, target) {
        let x = false,
            y = false,
            z = false;

        for(const [a, b, c] of triplets){
            x|= a === target[0] && b <= target[1] && c <= target[2];
            y|= a <= target[0] && b === target[1] && c <= target[2];
            z|= a <= target[0] && b <= target[1] && c === target[2];
            if( x && y && z) return true;
        }
        return false;
    }
}
