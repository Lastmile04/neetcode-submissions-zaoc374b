class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq_map = defaultdict(int)
        for i in range(len(nums)):
            freq_map[nums[i]]+=1
        return max(freq_map, key=freq_map.get)
        