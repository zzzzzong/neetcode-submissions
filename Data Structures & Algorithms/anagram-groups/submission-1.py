class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hashmap = {}
        
        for i in strs:
            if str(sorted(i)) in hashmap:
                hashmap[str(sorted(i))].append(i)
            else:
                hashmap[str(sorted(i))] = [i]
        
        for i in hashmap.values():
            res.append(i)

        return res
