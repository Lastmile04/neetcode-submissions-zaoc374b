class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        total = n+m
        # add 1 for odd length to add one extra element on the left
        total_left = (total+1) // 2

        # initialize the partition position pointers
        l,r = 0, n

        while l<=r:
            # calculate the partiton counters
            i=l+(r-l)//2
            j=total_left-i

            # Define bonundaries
            L1 = float('-inf') if i==0 else nums1[i-1]
            R1 = float('inf') if i==n else nums1[i]

            L2 = float('-inf') if j==0 else nums2[j-1]
            R2 = float('inf') if j==m else nums2[j]

            # compare condition to check validity
            if L1 <= R2 and L2<= R1:
                if total%2 == 0:
                    return (max(L1,L2) + min(R1,R2))/2
                else:
                    return max(L1,L2)
            
            elif L1 > R2:
                r = i-1
            else:
                l = i+1 
