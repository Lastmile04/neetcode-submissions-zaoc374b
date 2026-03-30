class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        # x1, y1 = 0, 0
        for x, y in points:
            d = -((x)**2+(y)**2)
            heapq.heappush(maxHeap,(d, [x,y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        result = []
        for dist, point in maxHeap:
            result.append(point)

        return result





            
