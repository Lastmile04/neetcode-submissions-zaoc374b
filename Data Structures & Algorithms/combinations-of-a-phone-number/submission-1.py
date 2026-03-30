class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # prune/edge case
        if not digits:
            return []

        letters = {'2' : ['a', 'b', 'c'], 
                  '3' : ['d', 'e', 'f'],
                  '4' : ['g', 'h', 'i'], 
                  '5' : ['j', 'k', 'l'], 
                  '6' : ['m', 'n', 'o'],
                  '7' : ['p', 'q', 'r', 's'], 
                  '8' : ['t', 'u', 'v'], 
                  '9' : ['w', 'x', 'y', 'z']
        }

        res = []
        def dfs(start, path):

            # base case
            if len(digits) == len(path):
                res.append("".join(path))
                return    
            
            # choice
            d = digits[start]
            for ch in letters[d]: # first append the current index, then in recursion the next index will be appended
                path.append(ch)
                dfs(start+1, path)
                path.pop()
        
        dfs(0, [])
        return res
            



                        





            