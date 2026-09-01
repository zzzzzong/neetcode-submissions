import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Patient Sorting x greedy x binary search, time: O(nlogn), space: O()
        tails = []
        for num in nums:
            idx = bisect.bisect_left(tails, num)
            if idx == len(tails):
                tails.append(num)
            else:
                tails[idx] = num
        return len(tails)