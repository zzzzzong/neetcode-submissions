class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 2): # 剩不到三個數就不用跑了
            curr = nums[i]
            if curr > 0: break
            if i > 0 and curr == nums[i - 1]: continue
            
            # --- 額外剪枝優化 (面試加分點) ---
            if curr + nums[i + 1] + nums[i + 2] > 0: break # 太大了，後面沒戲
            if curr + nums[n - 2] + nums[n - 1] < 0: continue # 太小了，這輪跳過
            # ------------------------------

            left, right = i + 1, n - 1
            while left < right:
                s = curr + nums[left] + nums[right]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([curr, nums[left], nums[right]])
                    # 找到後直接移動並跳過重複
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
