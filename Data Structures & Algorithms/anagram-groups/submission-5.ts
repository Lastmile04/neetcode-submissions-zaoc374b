class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs: string[]): string[][] {
        const res: Map<string, string[]> = new Map();
        for (const str of strs) {
            const count: number[] = Array.from({ length: 26 }, () => 0);

            for (const ch of str) {
                count[ch.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
            }

            const key: string = count.join('#');

            if (!res.has(key)) res.set(key, []);
            res.get(key)!.push(str);

        }

        return [...res.values()];
    }
}
