class Solution {
    /**
     * @param {string} s
     * @param {number} k
     * @return {number}
     */
    characterReplacement(s: string, k: number): number {
        let l = 0,
            res = 0,
            maxFreq = 0;
        const Fmap = new Map<string, number>();

        for (let r = 0; r < s.length; r++) {
            const ch = s[r];
            Fmap.set(ch, (Fmap.get(ch) ?? 0) + 1);

            maxFreq = Math.max(maxFreq, Fmap.get(ch)!);

            while ((r - l + 1) - maxFreq > k) {
                Fmap.set(s[l], Fmap.get(s[l])! - 1);
                l++;
            }
            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}
