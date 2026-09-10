class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        n = len(nums)
        ans = []
        nums.sort()  # O(nlogn)

        for a in range(n - 2):
            if nums[a] > 0: break
            if nums[a] + nums[-1] + nums[-2] < 0: continue
            if a > 0 and nums[a] == nums[a - 1]: continue
            
            
            b, c = a + 1, n - 1

            while b < c:
                sum_val = nums[a] + nums[b] + nums[c]
                if sum_val == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1

                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1

                elif sum_val < 0:
                    b += 1
                else:
                    c -= 1

        return ans