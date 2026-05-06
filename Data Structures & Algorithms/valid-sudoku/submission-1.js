class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const rowLen = board.length;
        const colLen = board[0].length;
        const rows = Array.from({ length: rowLen }, () => new Set());
        const cols = Array.from({ length: colLen }, () => new Set());
        const boxes = Array.from({ length: 9 }, () => new Set());

        for(let r = 0; r<rowLen; r++){
            for(let c = 0; c<colLen; c++){
                if(board[r][c] === '.') continue;

                const val = board[r][c];
                const box = Math.floor(r/3) * 3 + Math.floor(c/3);
                
                if(rows[r].has(val) || cols[c].has(val) || boxes[box].has(val)) return false;

                cols[c].add(val);
                rows[r].add(val);
                boxes[box].add(val);
            }
        }
        return true;
    }
}