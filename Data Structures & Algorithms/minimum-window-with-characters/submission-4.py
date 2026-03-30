class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        need = Counter(t)
        need_count = len(need)
        have = 0
        res = [-1, -1]
        res_len = float('inf')
        l = 0
        for r in range(len(s)):
            # add the current char count to window count
            window[s[r]] +=1
            # update have if the current character mathches to the one that we need
            if s[r] in need and window[s[r]] == need[s[r]]:
                have+=1
            #shrink window till invalid
            while need_count == have:
                # since the window is valid update the result to get the minimum length result
                if(r-l+1) < res_len:
                    res = [l,r]
                    res_len = r-l+1
                # shrink window 
                window[s[l]] -=1
                # to make window invalid again remove the left pointer count from h then n>h
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -=1
                l+=1
        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""