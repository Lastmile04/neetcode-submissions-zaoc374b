class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in hash_map:
                return[hash_map[complement]+1, i+1]
            else:
                hash_map[num] = i