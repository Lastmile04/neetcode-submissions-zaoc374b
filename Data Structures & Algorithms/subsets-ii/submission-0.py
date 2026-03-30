class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # brings duplicates together
        res = set()
        subset = []

        # start with empty subset
        res.add(tuple(subset))

        for num in nums:
            # snapshot of current unique subsets
            current = list(res)
            for tup in current:
                # create new subset by adding current element
                new_subset = list(tup) + [num]
                res.add(tuple(new_subset))

        # convert tuples back to lists
        return [list(t) for t in res]