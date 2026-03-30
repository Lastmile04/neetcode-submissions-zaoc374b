class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # since the entire matrix is sorted treat is as a single array or a 1d array
        # get the total number of element by row * column 
        # row
        m = len(matrix)
        # column
        n = len(matrix[0])
        l=0
        r=m*n-1
        while l<=r:
            mid = l+(r-l)//2
            # index exist in which row
            row = mid//n
            # which position inside the row
            col = mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r=mid-1
            else:
                l=mid+1
        return False