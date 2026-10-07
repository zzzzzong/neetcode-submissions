class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy, sell = prices[0], prices[0]
        ans = 0

        for i in range(1, n):
            if prices[i] < buy:
                if sell - buy > ans:
                    ans = sell - buy
                buy = prices[i]
                sell = prices[i]
                continue

            if prices[i] > sell:
                sell = prices[i]
    
        if sell - buy > ans:
            ans = sell - buy
        
        return ans