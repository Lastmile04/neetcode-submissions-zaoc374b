class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            sorted_label = " ".join(sorted(s))
            if sorted_label not in groups:
                groups[sorted_label] = []
            groups[sorted_label].append(s)
        return list(groups.values())