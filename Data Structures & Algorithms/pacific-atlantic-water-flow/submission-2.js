/*
 * Steps for this problem:
 * 1-> make a direction array for traversal to 4 sides if i want to use the bfs traversal
 * 2-> have to make sure only borders are targeted 
 * 3-> have to make sure when targeting borders no border should be repeated
 * 4-> make separate list of cells bordering each ocean
 * 5-> try to find which cell can be reached form the ocean, only traverse if the height is greater then current height
 * 6-> make resulting array for both oceans, if an element is in both array then it is the result  
 * 
 * I can start from the borders but how can i make sure that which cell's water is reaching both the oceans
 * do i make separate list for cells bordering both oceans, but what can it do
 * I can do the traversal in reverse only moving to the next cell if it is bigger, and the end element they reach in the end of their path can be marked as already visited so that it is not visited again 
 * */


class Solution {
    /**
     * @param {number[][]} heights
     * @return {number[][]}
     */
    pacificAtlantic(heights) {

        let rows = heights.length;
        let cols = heights[0].length;

        let pacific = Array.from({length:rows}, ()=>Array(cols).fill(false)); 
        let atlantic = Array.from({length:rows}, ()=>Array(cols).fill(false));

        const dfs = (r, c, visited)=>{
            visited[r][c] = true;
            let directions = [[1,0], [-1,0], [0,1], [0,-1]];
            for(let [dr, dc] of directions){
                let nr = r + dr,
                    nc = c + dc;
                if( nr >= 0 && nr < rows && nc >= 0 && nc < cols && !visited[nr][nc] && heights[nr][nc] >= heights[r][c]){
                    dfs(nr, nc, visited);
                }
            }
        };
        for( let c = 0 ; c< cols; c++){
            dfs(0, c, pacific);
            dfs(rows - 1, c, atlantic);
        }
        
        for( let r = 0 ; r < rows; r++){
            dfs(r, 0, pacific);
            dfs(r , cols -1 , atlantic);
        }
        
        let res = [];
        for(let r = 0; r < rows; r++){
            for(let c = 0; c < cols; c++){
                if(pacific[r][c] && atlantic[r][c]){
                    res.push([r,c]);
                }
            }
        }
        return res;    
    }
}

