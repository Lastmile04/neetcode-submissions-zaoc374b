class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let [l, r] = [0, heights.length-1]
        let maxArea = 0
        while (l < r){ 
            const area = Math.min(heights[l], heights[r]) * (r-l)
            maxArea = Math.max(maxArea, area)
            if(heights[l] < heights[r])  l+=1
            else r-=1
        }
        return maxArea

    }
}
