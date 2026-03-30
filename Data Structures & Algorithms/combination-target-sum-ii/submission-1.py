class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list to handle duplicates
        candidates.sort()

        res = []
        def backtrack(i, path, total):
            # base case
            if total == target:
                res.append(path.copy()) # take a snapshot of the current path
                return
            
            if total > target or i == len(candidates):
                return
            
            # include candidates[i]
            path.append(candidates[i])
            backtrack(i+1, path, total + candidates[i])
            path.pop()

            # skip candidates[i]
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, path, total)
        backtrack(0, [], 0)
        return res