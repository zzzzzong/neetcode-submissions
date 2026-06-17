class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        res = []

        for i in strs:
            key = "".join(sorted(i))

            if key in hashmap:
                hashmap[key].append(i)
            else:
                hashmap[key] = [i]
        
        for j in hashmap.values():
            res.append(j)
        
        return res