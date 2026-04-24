class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        
        const res = Array.from({length: temperatures.length}, () => 0);
        const stack = []; // pair: [temp, index]

        for (let i = 0; i < temperatures.length; i++){
            const t = temperatures[i];
            while(stack.length > 0 && t > stack[stack.length-1][0]){
                const [_, idx] = stack.pop();
                res[idx] = i - idx;
            }
            stack.push([t, i]);
        }
        return res;
    }
}
