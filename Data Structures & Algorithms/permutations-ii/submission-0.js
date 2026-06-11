class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    permuteUnique(nums) {
        nums.sort((a,b)=> a-b);
        const result = [];
        const used = Array.from({length : nums.length}, ()=> false)

        function backtrack(path){
            if(path.length === nums.length){
                // have to take a snapshot since array passby reference, so if only path is pushed then changes made to it would also
                // change the elements inside the result, making it just array of empty arrays
                result.push([...path]);
                return;
            }

            for(let i = 0; i<nums.length; i++){
                // to prevent illegal move of putting the same element twice since we need all the elements to create a permutation
                if(used[i]=== true) continue;

                // to skip duplicate elements 
                if( 
                    i > 0 &&
                    nums[i] === nums[i-1] &&
                    !used[i-1] 
                ) continue;
                // choice
                path.push(nums[i]);
                used[i] = true;
                
                // recurse
                backtrack(path);

                //undo
                path.pop();
                used[i]=false;
            }
        }

        backtrack([]);
        return result;
    }
}
