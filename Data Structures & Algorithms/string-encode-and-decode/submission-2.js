class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        for(let i = 0; i< strs.length; i++){
            const len = strs[i].length;
            strs[i] = `${len}:${strs[i]}`;
        }
        return strs.join('');
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let strs = [];
        let offset = 0;
        let strLen = str.length;
    
        while(offset < strLen ){
            let len = 0;

            while(offset < strLen && str[offset] != ':'){
                len = len * 10 + Number(str[offset]);
                offset++;
            }
            offset++;
            const word = str.slice(offset, offset+len);
            strs.push(word);
            offset+=len;
        }
        return strs;
    }
}
