class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            freq_map[s[r]] += 1
            win_size = r-l+1
            max_freq = max(freq_map.values())
            if win_size - max_freq <= k:
                res = max(res, win_size)
                continue
            else:
                freq_map[s[l]]-=1
                l+=1
        return res

