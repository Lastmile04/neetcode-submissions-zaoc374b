class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c=0
        nMap = defaultdict(int)
        l = 0
        for r in range(len(s)):
            nMap[s[r]] +=1
            while (r - l + 1) - max(nMap.values()) > k:
                nMap[s[l]] -= 1
                l += 1
            c = max(c, r - l + 1)
        return c
