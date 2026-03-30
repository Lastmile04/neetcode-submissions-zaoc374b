class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_map[s[i]] +=1
            t_map[t[i]] +=1
        if s_map == t_map:
            return True
        return False