class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        index_map = {}
        for i, n in enumerate(nums):
            if n in index_map:
                return True
            else:
                index_map[n] = i
        return False