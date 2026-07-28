class Solution {
    /**
     * @param {number[]} people
     * @param {number} limit
     * @return {number}
     */
    numRescueBoats(people: number[], limit: number): number {
        if ( limit === 1) return people.length;
        people.sort((a,b)=>a-b);
        let l = 0,
            r = people.length -1;
        let res = 0;
        while(l<=r){
            const total_weight = people[l] + people[r];
            if(total_weight <= limit){
                res++;
                l++;
                r--;
            } else {
                res++;
                r--;
            }
        }
        return res;
    }
}
