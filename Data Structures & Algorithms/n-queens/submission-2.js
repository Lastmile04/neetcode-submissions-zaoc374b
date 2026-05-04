class Solution {
    /**
     * @param {number} n
     * @return {string[][]}
     */
    solveNQueens(n) {
        const cols = new Set();
        const posDiag = new Set();
        const negDiag = new Set();

        const res = [];
        const board = Array.from({length:n}, ()=> new Array(n).fill('.'));

        const dfs = (r)=>{
            // base case
            if(r === n){
                res.push( board.map((row)=> row.join('')));
                return;
            }

            for( let c = 0; c < n; c++){
                // skip case ( cases to avoid placement of queen )
                if( cols.has(c) || posDiag.has(r+c) || negDiag.has(r-c)) continue;

                cols.add(c);
                negDiag.add(r-c);
                posDiag.add(r+c);
                board[r][c] = 'Q';

                dfs(r+1);

                cols.delete(c);
                negDiag.delete(r-c);
                posDiag.delete(r+c);
                board[r][c] = '.';
            }
        }

        dfs(0);
        return res;
    }
}
