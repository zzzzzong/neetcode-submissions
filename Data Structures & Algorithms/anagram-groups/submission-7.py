from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []

        for i in strs:
            key = "".join(sorted(i))

            if key in hmap:
                hmap[key].append(i)
            else:
                hmap[key] = [i]
        
        return list(hmap.values())