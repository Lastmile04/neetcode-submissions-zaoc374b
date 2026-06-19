class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    decodeString(s) {
        let k = 0;
        let currStr = "";

        const countStack = [];
        const strStack = [];

        for(const ch of s){
            if(ch >= '0' && ch <= '9'){
                k = k * 10+Number(ch);
            } else if(ch === '['){
                countStack.push(k);
                strStack.push(currStr);
                currStr = '';
                k = 0;
            } else if(ch === ']'){
                const temp = currStr;
                currStr = strStack.pop();
                const count = countStack.pop();
                currStr += temp.repeat(count);
            }else{
                currStr+= ch
            }

        }
        return currStr;
        
    }
}
