class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        nums.sort()
        n = len(nums)
        res = []

        for pivot in range(n - 2):
            # pruning
            if nums[pivot] > 0:
                break
            if pivot > 0 and nums[pivot] == nums[pivot - 1]:
                continue
            if nums[pivot] + nums[-2] + nums[-1] < 0:
                continue
            
            left = pivot + 1
            right = n - 1

            while left < right:
                summ = nums[pivot] + nums[left] + nums[right]
                if summ == 0:
                    res.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif summ < 0:
                    left += 1
                
                else:
                    right -= 1
            
        return res