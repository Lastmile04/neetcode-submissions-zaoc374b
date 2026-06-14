class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const stack = [];

        const operations = {
            '+' : (a,b)=> a+b,
            '-' : (a,b)=> a-b,
            '*' : (a,b)=> a*b,
            '/' : (a,b)=> Math.trunc(a/b),
        }

        for(const t of tokens){
            if(operations[t]){
                const b = Number(stack.pop());
                const a = Number(stack.pop());

                const res = operations[t](a,b);
                stack.push(res);
            } else {
                stack.push(Number(t))
            }
        }
        return stack[0];
    }
}
