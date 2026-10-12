func maxProfit(prices []int) int {
	buy, sell := 0, 0 // the index
	ans := 0
	
	for idx, val := range prices {
		if val < prices[buy] {
			if prices[sell] - prices[buy] > ans {
				ans = prices[sell] - prices[buy]
			}

			buy, sell = idx, idx
		}
		if val > prices[sell] {
			sell = idx
		}
	}
	if prices[sell] - prices[buy] > ans {
		ans = prices[sell] - prices[buy]
	}

	return ans
}
