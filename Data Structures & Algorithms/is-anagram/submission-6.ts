class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const rearrange = (str:string)=>{
            return str.split('').sort().join('')
        }
        return rearrange(s) === rearrange(t);
    }
}
