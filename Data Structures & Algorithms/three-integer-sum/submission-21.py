class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        n = len(nums)
        ans = []
        nums.sort()

        for pivot in range(n - 2):
            if nums[pivot] + nums[n-1] + nums[n-2] < 0: continue
            if pivot > 0 and nums[pivot] == nums[pivot-1]: continue
            if nums[pivot] > 0: break

            left, right = pivot + 1, n - 1

            while left < right:
                cur_sum = nums[pivot] + nums[left] + nums[right]

                if cur_sum == 0:
                    ans.append([nums[pivot], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    right -= 1
                    while left < right and nums[right] == nums[right+1]:
                        right -=1
                    continue
                
                if cur_sum < 0:
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    continue
                
                right -= 1
                while left < right and nums[right] == nums[right+1]:
                    right -=1
        
        return ans