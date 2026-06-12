class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    maxTurbulenceSize(arr) {
        let l = 0,
            r = 1,
            res = 1,
            prev = '';
        
        while(r < arr.length){
            if(arr[r-1] > arr[r] && prev !== '>'){
                res = Math.max(res, r-l+1);
                r++;
                prev = '>';
            } else if(arr[r-1] < arr[r] && prev !== '<'){
                res = Math.max(res, r-l+1);
                r++;
                prev = '<';
            } else{
                r = arr[r] === arr[r-1] ? r+1 : r;
                l = r-1;
                prev = '';
            }
        }
        return res;

    }    
}
