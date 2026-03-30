class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        curr_arr = []
        n = len(nums)
        for i in range(k):
            curr_arr.append(nums[i])
        res.append(max(curr_arr))

        for i in range(k,n):
            curr_arr.append(nums[i])
            curr_arr.pop(0)
            res.append(max(curr_arr))
        return res