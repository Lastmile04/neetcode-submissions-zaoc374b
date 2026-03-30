class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs( idx, subset, curr_ttl):
            # base case
            if curr_ttl - target == 0:
                res.append(subset.copy())
                return

            # choice
            for i in range(idx, len(candidates)):
                # termination constraint
                # skip duplicate
                if i > idx and candidates[i] == candidates[i-1]:
                    continue

                # prune wrong branch
                if curr_ttl + candidates[i] > target:
                    break

                # choice and backtrack
                subset.append(candidates[i])
                dfs(i+1, subset, curr_ttl + candidates[i])
                subset.pop()
        dfs(0, [], 0)
        return res