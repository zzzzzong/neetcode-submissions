class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
    
class PrefixTree:
    # 這本質上就是n-nary tree, dict tree, prefix tree 都差不多。本質上就是dict包著dict這樣
    # 反正就是逐個字母檢查, 有key就走進去, 沒有就創一個key對應的dict之後再走進去
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True