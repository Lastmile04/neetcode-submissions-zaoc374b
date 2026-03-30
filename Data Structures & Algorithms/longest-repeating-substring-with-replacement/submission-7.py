class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freq_map = defaultdict(int)
        max_freq = 0
        res = 0
        for r in range(len(s)):
            freq_map[s[r]] +=1
            win_size =  r-l+1
            max_freq = max(max_freq, freq_map[s[r]])
            if win_size - max_freq > k:
                freq_map[s[l]] -=1
                l+=1
            res = r-l+1
        return res


       



