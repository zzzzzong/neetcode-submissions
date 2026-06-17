class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        hmap = {}

        for word in strs:
            key = [0] * 26
            for letter in word:
                key[ord(letter) - ord('a')] += 1
            
            k = tuple(key)
            if k in hmap:
                hmap[k].append(word)
            else:
                hmap[k] = [word]
        
        for group in hmap:
            res.append(hmap[group])
        
        return res