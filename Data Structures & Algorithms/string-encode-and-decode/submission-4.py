class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        
        while i < n:
            # 尋找分隔符 '#'
            j = i
            while s[j] != '#':
                j += 1
            
            # 解析長度並將指標移到單字起點
            length = int(s[i:j])
            i = j + 1
            
            # 使用切片直接取出整個單字，避免逐字拼接
            res.append(s[i : i + length])
            
            # 指標跳到下一個長度標記的起點
            i += length
            
        return res