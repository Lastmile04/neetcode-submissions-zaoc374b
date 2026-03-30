class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i]+nums[j]+nums[k]
                    if sum == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()
                        res.add(tuple(triplet))
        final_res = [list(t) for t in res]
        return final_res
