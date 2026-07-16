class MyHashSet:
    # boolean array, time: O(1), space: O(n)

    def __init__(self):
        self.data = [False] * 1000001  # this is for the test cases range


    def add(self, key: int) -> None:
        self.data[key] = True

    def remove(self, key: int) -> None:
        self.data[key] = False

    def contains(self, key: int) -> bool:
        return self.data[key]

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)