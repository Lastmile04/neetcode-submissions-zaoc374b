class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    decodeString(s: string): string {

        const char = [];
        const num = [];

        let cur = '',
            k = 0; // multiplier 

        for (const ch of s) {
            if (ch >= '0' && ch <= '9') k = k * 10 + Number(ch);
            else if (ch === '[') {
                // push both to stack
                num.push(k);
                char.push(cur);
                // reset the current string and multiplier
                cur = '';
                k = 0;
            }
            else if (ch === ']') {
                const temp = cur;
                cur = char.pop()!;
                const count = num.pop()!;
                cur += temp.repeat(count);
            }
            else cur += ch;
        }
        return cur;
    }
}
