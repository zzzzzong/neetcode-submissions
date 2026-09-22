class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hmap x sort, time: O(m * nlogn), space: O(n)

        hmap = {}
        ans = []

        for word in strs:
            key = ''.join(sorted(word))
            if key not in hmap:
                hmap[key] = []
            hmap[key].append(word)
        
        for i in hmap:
            ans.append(hmap[i])
        
        return ans