class Solution {
    /**
     * @param {string} s
     * @return {string}
     */
    reorganizeString(s: string): string {
        const charMap = Array.from({ length: 26 }, () => 0);
        const aCode = 'a'.charCodeAt(0);

        for (const ch of s) {
            const idx = ch.charCodeAt(0) - aCode;
            charMap[idx]++;
        }

        let maxF = 0;
        let maxIdx = -1;
        for (let i = 0; i < charMap.length; i++) {
            if (charMap[i] > maxF) {
                maxF = charMap[i];
                maxIdx = i;
            }
        }

        if (maxF > Math.ceil(s.length / 2)) return "";

        const res = new Array(s.length);
        let idx = 0;

        const maxChar = String.fromCharCode(maxIdx + aCode);
        while (charMap[maxIdx] > 0) {
            res[idx] = maxChar;
            idx += 2;
            charMap[maxIdx]--;
        }

        for (let i = 0; i < 26; i++) {
            while (charMap[i] > 0) {
                // Wrap around to the first odd index if we exceed the array length
                if (idx >= res.length) {
                    idx = 1;
                }
                res[idx] = String.fromCharCode(i + aCode);
                idx += 2;
                charMap[i]--;
            }
        }

        return res.join('');
    }
}