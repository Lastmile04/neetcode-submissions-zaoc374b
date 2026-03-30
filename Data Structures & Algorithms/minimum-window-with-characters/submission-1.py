class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        n = len(s)
        res = ""
        for w in range(len(t), n+1):
            win_count = Counter()
            #first window
            for i in range(w):
                win_count[s[i]] +=1

            valid = True
            for ch in t_count:
                if win_count[ch] < t_count[ch]:
                    valid = False
                    break
            if valid:
                res = s[0:w]
                break
            
            #slide Window
            for i in range(w,n):
                win_count[s[i]] +=1
                win_count[s[i-w]] -=1
                valid = True
                for ch in t_count:
                    if win_count[ch] < t_count[ch]:
                        valid = False
                        break
                if valid:
                    res = s[i-w+1:i+1]
                    break
            if res:
                break
        return res





        