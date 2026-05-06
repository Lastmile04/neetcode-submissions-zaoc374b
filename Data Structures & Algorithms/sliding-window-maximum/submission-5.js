class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    // deque store indices
    maxSlidingWindow(nums, k) {
        const deque = [];
        let front = 0;

        let res = [];

        let l = 0; 

        for (let r = 0; r < nums.length; r++) {
            // maintain decreasing order
            while( deque.length > front && nums[deque[deque.length-1]] < nums[r]){
                deque.pop();
            }
            // add new indices 
            deque.push(r); 
            
            //remove expired indices
            if(deque[front] < l) front++;

            // record result on valid window
            if( r-l+1 === k ){
                res.push(nums[deque[front]]);
                l++;
            } 
        }
        return res;
    } 
}