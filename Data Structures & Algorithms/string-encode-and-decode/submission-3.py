class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in strs:
            res += str(len(i)) + '#' + i

        return res

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []

        while i < n:
            
            tmp = ''
            while s[i] != '#':
                tmp += s[i]
                i += 1
            
            length = int(tmp)
            i += 1

            word = ''
            for _ in range(length):
                word += s[i]
                i += 1
            
            res.append(word)
        
        return res