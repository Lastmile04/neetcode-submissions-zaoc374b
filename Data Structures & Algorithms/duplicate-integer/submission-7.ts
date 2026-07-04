class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        const fMap:Map<number, number> = new Map();

        for(const n of nums){
            fMap.set(n, (fMap.get(n) ?? 0) +1);
        }

        for(const f of fMap.values()){
            if(f > 1) return true;
        }

        return false;
    }
}
