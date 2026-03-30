class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_count = 0
        for i in range(len(s)):
            hashSet = set()
            count = 0
            for j in range(i, len(s)):
                if s[j] in hashSet:
                    break
                else:
                    hashSet.add(s[j])
                    count += 1
                    max_count = max(count, max_count)
        return max_count