class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for i in range(len(nums)):
            freq_map[nums[i]]+=1
        print(freq_map)
        heap = []
        for num in freq_map.keys():
            heapq.heappush(heap, (freq_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
        
