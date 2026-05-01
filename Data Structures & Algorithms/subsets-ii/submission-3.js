class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    subsetsWithDup(nums) {
        const res = [];
        nums.sort((a, b)=> (a - b));

        const dfs = (subset, i)=>{
            res.push([...subset]);
            for(let j = i; j < nums.length; j++ ){
                // base case
                if( j > i && nums[j] === nums[j-1]) continue;

                subset.push(nums[j]);
                dfs(subset, j+1);
                subset.pop();
            }
        }
        dfs([],0);
        return res;
    }
}
