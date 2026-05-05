class Solution {
    /**
     * @param {number[]} height
     * @return {number}
     */
    trap(height) {
        let total = 0;

        let l = 0,
            r = height.length - 1;

        let maxL = height[l],
            maxR = height[r];

        while(l<r){
            if(maxL < maxR){
                // at any point the smaller side is the limiting factor that's why larger side is ignored
                l++;
                maxL = Math.max(maxL, height[l]);
                total += maxL - height[l];
            }else{
                r--;
                maxR = Math.max(maxR, height[r]);
                total += maxR - height[r];
            }

        }
        return total;
    }
}