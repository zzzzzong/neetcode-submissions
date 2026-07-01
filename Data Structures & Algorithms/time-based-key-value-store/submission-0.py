class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.data:
            self.data[key].append([value, timestamp])
        else:
            self.data[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ''

        # binary search
        # because the question ensured the time stamp is strictly increasing.
        res = ''
        left = 0
        right = len(self.data[key]) - 1

        while left <= right:
            mid = left + (right - left) // 2
            
            if self.data[key][mid][1] == timestamp:
                return self.data[key][mid][0]
            
            elif self.data[key][mid][1] < timestamp:
                res = self.data[key][mid][0]  # the question ask if can't find the target
                                            # gonna return the max time stamp which is <= target
                left = mid + 1
            
            else:
                right = mid - 1
        
        return res
