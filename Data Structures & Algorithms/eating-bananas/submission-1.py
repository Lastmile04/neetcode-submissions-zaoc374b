class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # since in the brute force approach as we see that the total time decreases as the speed increases so we can use sorted search space from 1 to max(piles) using binary search
        l=1
        # upper bound and lower bound of range in which the minimum speed required for koko to eat banana lies
        r=max(piles)
        # since if no minimum value is found then the only min is the max value of piles
        res=r
        while l<=r:
            # speed at which koko eats the banana
            k = l+(r-l)//2
            # total time taken to finish the pile
            toatlTime = 0
            for p in piles:
                toatlTime+= math.ceil(p/k)
            if toatlTime <=h:
                res = k
                r = k-1
            else:
                l = k+1
        return res
               
