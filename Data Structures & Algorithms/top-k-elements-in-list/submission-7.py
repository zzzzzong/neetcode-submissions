class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket x hashmap, time: O(3n), space: O(n)
        hmap = {}

        for char in nums:
            if char not in hmap:
                hmap[char] = 1
                continue
            hmap[char] += 1

        buckets = [[] for _ in range(len(nums) + 1)] # might have zero freq

        for key in hmap:   # freq == hmap's value
            buckets[hmap[key]].append(key)

        ans = []
        for i in range(len(buckets) - 1, 0, -1):
            for number in buckets[i]:
                ans.append(number)
                if len(ans) == k:
                    return ans