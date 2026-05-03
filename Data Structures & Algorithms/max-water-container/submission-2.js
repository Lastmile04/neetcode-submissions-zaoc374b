class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let l = 0,
            r = heights.length-1;
        let maxCap = 0;
        while(l<r){
            const width = r-l;
            const height = Math.min(heights[l], heights[r]);
            const cap = height * width;
            maxCap = Math.max(cap, maxCap);

            if(heights[l] > heights[r]) r--;
            else l++;
        }
        return maxCap;
    }
}