class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        nums = list(set(nums))
        nums.sort()
        curr = 1
        m = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                curr+=1
                m = max(curr, m)
            else:
                curr = 1
        return m
