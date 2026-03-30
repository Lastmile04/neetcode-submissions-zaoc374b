class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        needCount = len(need)
        have = 0
        l=0
        window = defaultdict(int)
        res = [-1,-1]
        res_len = float("inf")
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            if ch in need and window[ch] == need[ch]:
                have +=1
            while have == needCount:
                if (r-l +1) < res_len:
                    res = [l,r]
                    res_len = r-l +1
                window[s[l]] -=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if res_len != float("inf") else ""

                






        