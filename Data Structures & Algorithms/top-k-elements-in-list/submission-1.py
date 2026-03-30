class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] +=1
        sortedItems = sorted(freq_map.items(), key = lambda x: x[1], reverse= True)
        return [num for num, count in sortedItems[:k]]
