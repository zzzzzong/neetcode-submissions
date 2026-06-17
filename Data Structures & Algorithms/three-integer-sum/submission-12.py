class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        n = len(nums)
        nums.sort()
        res = []

        for a in range(n - 2):
            if nums[a] > 0:
                break
            if nums[a] + nums[-2] + nums[-1] < 0:
                continue
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            
            b = a + 1
            c = n - 1

            while b < c:
                summ = nums[a] + nums[b] + nums[c]
                if summ == 0:
                    res.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                
                elif summ < 0:
                    b += 1
                else:
                    c -= 1
        
        return res