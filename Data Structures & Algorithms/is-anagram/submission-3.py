class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_mapS = {}
        freq_mapT = {}
        
        for char in s:
            freq_mapS[char] = freq_mapS.get(char, 0) + 1
        
        for char in t:
            freq_mapT[char] = freq_mapT.get(char, 0) + 1
        
        if freq_mapS == freq_mapT:
            return True
        else:
            return False