
class Solution {
    /**
     * @param {number[]} numbers
     * @param {number} target
     * @return {number[]}
     */
    twoSum(numbers, target) {
        let l = 0,
            r = numbers.length-1;

        while(l<r){
            const temp = numbers[l]+numbers[r];
            if(temp > target) r-=1;
            else if (temp === target) return [l+1, r+1];
            else l+=1;
        }
    }
}
