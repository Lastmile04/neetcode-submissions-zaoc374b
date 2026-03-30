class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        longest = 0
        for n in nums:
            if (n-1) not in nums:
                len = 0
                while (n + len) in nums:
                    len +=1
                longest = max(longest, len)
        return longest
