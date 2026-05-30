class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    majorityElement(nums) {
        let co1=0,
            co2=0,
            c1,
            c2;

        for(let n of nums ){
            if(n===c1) co1++;
            else if(n===c2) co2++;
            else if(co1===0) {
                c1 = n;
                co1++;
            }
            else if(co2 === 0){
                c2 = n;
                co2++;
            }
            else{
                co1--;
                co2--;
            }
        }
        co1=0;
        co2=0;
        const res = [];
        for(let n of nums){
            if(n === c1) co1++;
            if(n === c2) co2++; 
        }
        if(co1 > Math.floor(nums.length/3)) res.push(c1);
        if(co2 > Math.floor(nums.length/3)) res.push(c2);
        return res;
    }
}
