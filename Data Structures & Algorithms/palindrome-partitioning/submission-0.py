class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def validPalindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def dfs(start, path):
            # base case
            if start == len(s):
                res.append(path.copy())
                return
            
            for i in range(start, len(s)):
                candidate = s[start:i+1]
                if not validPalindrome(candidate): continue # skip non-valid substrings
                path.append(candidate)  # add the current end point
                dfs(i+1, path)
                path.pop()

        dfs(0, [])
        return res
