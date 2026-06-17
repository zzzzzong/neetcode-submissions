class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

        # e.g. ["apple", "banana"] -> 5#apple6#banana

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j]) # to filter the "length" and the "#(number sign)"

            i = j + 1
            j = i + length # These two lines is to measure the length of string
            
            res.append(s[i:j])
            i = j

        return res