class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for n in range(len(numbers)):
            for m in range(1, len(numbers)):
                if numbers[n] + numbers[m] == target:
                    return[n+1,m+1]