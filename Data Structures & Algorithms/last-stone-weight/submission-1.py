class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        
        for stone in stones:
            heapq.heappush(maxHeap, -stone);
        
        while len(maxHeap) != 1:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x == y:
                if len(maxHeap) == 0: return 0
                else: continue
            elif x > y:
                val = x-y
                heapq.heappush(maxHeap, -val)
            else:
                continue
        return -maxHeap[0]

