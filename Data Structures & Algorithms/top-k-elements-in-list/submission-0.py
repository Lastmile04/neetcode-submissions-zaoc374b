class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        freq = [[] for i in range(len(nums)+1)]
        for n, c in count.items(): #count.items returns key value pair
            freq[c].append(n) #n is the number c is the count
        
        res=[]
        for i in range(len(freq) -1 , 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) ==k:
                    return res

        
        
            