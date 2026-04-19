

class Solution {
    /**
     * @param {number[][]} grid
     * @return {number}
     */
    orangesRotting(grid) {
		const q = [];
		let fresh = 0;
		let time = 0;
		
		let rows = grid.length;
		let cols = grid[0].length;
		
		for(let r = 0; r < rows; r++){
			for(let c = 0; c < cols; c++){
				
				if(grid[r][c] === 1) fresh++;
				if(grid[r][c] === 2) q.push([r,c]);
			}
		}
		const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]];
		while(fresh > 0 && q.length > 0){
			const length = q.length;
			for(let i = 0; i < length; i++){
				const [ currR, currC ] = q.shift();
				for(const [dr, dc] of directions){
					const row = currR + dr;
					const col = currC + dc;
					if(
						row >= 0 &&
						row < rows &&
						col >= 0 &&
						col < cols &&
						grid[row][col] === 1
					){
						grid[row][col] = 2;
						q.push([row, col]);
						fresh--;
					}
				
				}
			}
			time++;
		}
		return fresh === 0 ? time: -1;
		
	}
}
