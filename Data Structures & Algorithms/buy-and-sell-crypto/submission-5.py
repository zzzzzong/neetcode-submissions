class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sliding window, time: O(n), space: O(1)
        ans = 0
        buy, sell = prices[0], prices[0]

        for p in prices:
            if p > sell:
                sell = p
                continue
            if p < buy:
                profit = sell - buy
                if profit > ans:
                    ans = profit
                buy = p
                sell = p
        
        profit = sell - buy
        if profit > ans:
            return profit
        
        return ans