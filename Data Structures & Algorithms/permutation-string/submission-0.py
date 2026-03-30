class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1>n2: return False
        sorted_s1 = sorted(s1)
        for i in range(n2 - n1 + 1):
            curr_substring = s2[i:i+n1]
            sorted_substring = sorted(curr_substring)
            if sorted_substring == sorted_s1:
                return True
        return False


