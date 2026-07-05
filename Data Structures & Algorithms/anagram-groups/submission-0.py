from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s=defaultdict(list)
        for i in strs:
            j=''.join(sorted(i))
            s[j].append(i)
        return list(s.values())

        