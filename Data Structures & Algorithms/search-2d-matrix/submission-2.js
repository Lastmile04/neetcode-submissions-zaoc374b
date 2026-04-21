class Solution {
    /**
     * @param {number[][]} matrix
     * @param {number} target
     * @return {boolean}
     */
    searchMatrix(matrix, target) {
        const rows = matrix.length;
        const cols = matrix[0].length;

        let l = 0,
        r = rows * cols - 1;

        while(l <= r){
            const mid = l + Math.floor((r-l)/2);
            const row = Math.floor(mid / cols);
            const col = mid % cols;
            if(matrix[row][col] === target) return true;
            else if(matrix[row][col] > target) r = mid - 1;
            else l = mid + 1;
        }
        return false;
    }
}
