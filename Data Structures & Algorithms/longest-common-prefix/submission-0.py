class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorting, time: O(nlogn), space: O(n)
        # pruning
        if len(strs) == 1:
            return strs[0]
        
        # main logic
        strs = sorted(strs)
        
        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        
        return strs[0]