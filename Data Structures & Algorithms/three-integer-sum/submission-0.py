class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n):
            # 如果第一個數就大於 0，後面三個數相加不可能等於 0
            if nums[i] > 0:
                break
            
            # 【外層去重】：i > 0 是為了避免 i-1 變成 -1 抓到最後一個數
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            target = -nums[i]
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum > target:
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    # 找到一組答案
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 【內層去重】：如果下一個數字跟現在一樣，就繼續移動指標
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 找到新數字後，最後還要再移動一次，才會跳到下一組可能的組合
                    left += 1
                    right -= 1

        return res