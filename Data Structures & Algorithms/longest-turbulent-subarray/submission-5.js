class Solution {
    /**
     * @param {number[]} arr
     * @return {number}
     */
    maxTurbulenceSize(arr) {
        
        const compare = [];
        if(arr.length < 2) return 1;
        for(let i = 0; i<arr.length; i++){
            if(i > 0 && arr[i-1] > arr[i]) compare.push(">");
            if(i > 0 && arr[i-1] < arr[i]) compare.push("<");
            if(i > 0 && arr[i-1] === arr[i]) compare.push("==");
        }
        const len = [];
        let res = 1;

        for(let i = 0; i<compare.length; i++){
            if(compare[i] == ">" && res == 1) res+=1;
            if(compare[i] == "<" && res == 1) res+=1;

            if(
                 i > 0 &&
                compare[i-1] == ">" &&
                compare[i] == ">"
            ){
                len.push(res);
                res = 1;
                continue;
            }

            if(
                 i > 0 &&
                compare[i-1] == "<" &&
                compare[i] == "<"
            ){
                len.push(res);
                res = 1;
                continue;
            }

            if(compare[i] == "==") {
                len.push(res);
                res = 1;
                continue;
            }


            if( 
                i > 0 &&
                compare[i-1] == ">" &&
                compare[i] == "<" 
            ){
                res++;
            }

            if( 
                i > 0 &&
                compare[i-1] == "<" &&
                compare[i] == ">" 
            ){
                res++;
            }

        }
        return Math.max(...len, res);
    }
}
