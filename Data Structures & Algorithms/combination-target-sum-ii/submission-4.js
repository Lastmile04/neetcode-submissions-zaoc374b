class Solution {
    /**
     * @param {number[]} candidates
     * @param {number} target
     * @return {number[][]}
     */
    combinationSum2(candidates, target) {
		this.res = [];
		candidates.sort((a,b)=> a - b);
		
		const dfs = (idx, path, total)=>{
			// base case
			if( total === target){
				this.res.push([...path]);
				return;
			}
			
			for( let i = idx; i < candidates.length; i++){
				// skip duplicates
				if(i>idx && candidates[i] === candidates[i-1]) continue;
				
				// stop traversing forward 
				if(total + candidates[i] > target) break;
				
				path.push(candidates[i]);
				dfs(i+1, path, total + candidates[i]);
				path.pop();
			}
		};
		dfs(0, [], 0);
		return this.res;
	}
}
