class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                     # bring equal values together
        res = []                        # will hold the final subsets
        cur = []                        # current subset being built
    
        def backtrack(idx):
            # Every node in the decision tree corresponds to a valid subset
            res.append(cur.copy())      # store a snapshot of the current choice
    
            for i in range(idx, len(nums)):
                # Skip duplicates: if the current element equals the previous one
                # and we are at the same level (i > idx), then using it would
                # recreate a subset we already generated.
                if i > idx and nums[i] == nums[i - 1]:
                    continue
    
                # ── Include nums[i] ────────────────────────
                cur.append(nums[i])
                backtrack(i + 1)        # recurse with next index
                cur.pop()               # ── Exclude (backtrack) ────────
    
        backtrack(0)
        return res


