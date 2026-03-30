class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in index_map:
                return [index_map[comp], i]
            else:
                index_map[n] = i
                
        