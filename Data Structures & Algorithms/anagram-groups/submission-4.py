from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 使用 defaultdict 簡化初始化邏輯
        res = defaultdict(list)
        
        for s in strs:
            # 建立一個長度 26 的陣列計數 (假設只有小寫英文)
            count = [0] * 26 
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # 將 list 轉成 tuple，因為 tuple 是不可變的 (Immutable)，才能當 key
            res[tuple(count)].append(s)
            
        return list(res.values())