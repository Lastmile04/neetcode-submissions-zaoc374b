class Solution {
    /**
     * @param {number} a
     * @param {number} b
     * @param {number} c
     * @return {string}
     */
    longestDiverseString(a, b, c) {
        const count = [a, b, c];
        const res = [];

        const getMax = (repeated) => {
            let idx = -1;
            let maxCnt = 0;
            for (let i = 0; i < 3; i++) {
                if (i === repeated || count[i] === 0) {
                    continue;
                }
                if (maxCnt < count[i]) {
                    maxCnt = count[i];
                    idx = i;
                }
            }
            return idx;
        };

        let repeated = -1;
        while (true) {
            const maxChar = getMax(repeated);
            if (maxChar === -1) {
                break;
            }
            res.push(String.fromCharCode(maxChar + 97));
            count[maxChar]--;

            if (res.length > 1 && res[res.length - 1] === res[res.length - 2]) {
                repeated = maxChar;
            } else {
                repeated = -1;
            }
        }

        return res.join('');
    }
}