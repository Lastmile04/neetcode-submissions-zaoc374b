class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        # we need to find the start of the streak, how can we do that
        # if num-1 doesn't exist we consider that as start of a new streak
        longest = 0
        for num in nums:
            if num-1 not in nums:
                length = 1
                while (num + length) in nums:
                    length+=1
                longest = max(length, longest)
        return longest