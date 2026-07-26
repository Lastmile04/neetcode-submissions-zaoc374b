class Solution {
    /**
     * @param {number[]} fruits
     * @return {number}
     */
    totalFruit(fruits: number[]): number {
        const f_map: Map<number, number> = new Map();
        let maxFruits = 0;
        let l = 0;
        for (let r = 0; r<fruits.length; r++){
            f_map.set(fruits[r], (f_map.get(fruits[r]) || 0) + 1);
            while(f_map.size > 2){
                const count = f_map.get(fruits[l])!;
                
                if(count === 1) f_map.delete(fruits[l]);
                else f_map.set(fruits[l], count -1);
                l++;
            }

            maxFruits = Math.max(maxFruits, r-l+1);
        }
        return maxFruits;
    }
}
