class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        
        median = 0
        l, r = 0, len(nums)-1
        if len(nums)%2 == 0:
            mid1 = l+(r-l)//2
            l+=1
            mid2= l+(r-l)//2
            median = (nums[mid1]+nums[mid2])/2
        else:
            mid = l+(r-l)//2
            median = nums[mid]
        return median