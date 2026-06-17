class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}

        for i in strs:
            key = str(sorted(i))
            if key in hmap:
                hmap[key].append(i)
            else:
                hmap[key] = [i]
        
        res = []

        for i in hmap:
            res.append(hmap[i])
        
        return res