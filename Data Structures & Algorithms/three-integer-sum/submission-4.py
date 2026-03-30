class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            index_map = {}
            target_sum = -nums[i]
            j = i+1
            while j <len(nums):
                comp = target_sum - nums[j]

                if comp in index_map:
                    res.append([nums[i], comp, nums[j]])

                    while j+1 < len(nums) and nums[j] == nums[j+1]:
                        j+=1

                index_map[nums[j]] = j
                j+=1
        return res