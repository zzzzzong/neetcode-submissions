class KthLargest:
    # sorting method, time: O(m * nlogn), space = O(m) m is the extra space
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort() # O(nlogn)

        return self.arr[len(self.arr) - self.k]
