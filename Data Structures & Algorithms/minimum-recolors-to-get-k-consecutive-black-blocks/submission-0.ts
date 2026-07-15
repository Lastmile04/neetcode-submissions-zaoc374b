class Solution {
    /**
     * @param {string} blocks
     * @param {number} k
     * @return {number}
     */
    minimumRecolors(blocks: string, k: number): number {
        let l = 0;
	    let minCount: number = Infinity;
       let count = 0;
	    for(let r = 0; r<blocks.length; r++){
	        if(blocks[r] === "W") count++;
	        if(r-l+1 >= k){
	            minCount = Math.min(minCount, count);
	            if(blocks[l] === "W") count--;
	            l++;
	        }
	    }
	    return minCount;
    }
}
