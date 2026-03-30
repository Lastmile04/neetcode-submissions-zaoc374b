class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {

        let valid = new Map([ [')', '('], ['}', '{'], [ ']', '['] ]);
        let stack = []

        for(let i = 0; i<s.length; i++){
            if(valid.has(s[i])){
                if(!stack || stack[stack.length-1] !== valid.get(s[i])) return false
                else stack.pop()
            }
            else stack.push(s[i])
        }
        return stack.length === 0
    }
}
