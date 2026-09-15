class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        hmap = {}

        for word in strs:
            counter = [0] * 26
            for letter in word:
                counter[ord(letter) - ord('a')] += 1
            
            key = tuple(counter)
            if key in hmap:
                hmap[key].append(word)
                continue
            hmap[key] = [word]
        
        for i in hmap:
            ans.append(hmap[i])

        return ans