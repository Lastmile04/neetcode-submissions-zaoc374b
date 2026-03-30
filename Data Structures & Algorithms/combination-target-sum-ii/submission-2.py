class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort the list to handle duplicates
        candidates.sort()

        res = []
        def backtrack(idx, path, total):
            # base case
            if total == target:
                res.append(path.copy()) # take a snapshot of the current path
                return
            
            for i in range(idx, len(candidates)):
                # skip duplicate
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                # break if total exceed target
                if total + candidates[i] > target:
                    break;
                
                # noraml append and backtrack
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])
                path.pop()
        backtrack(0, [], 0)
        return res