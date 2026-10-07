func maxProfit(prices []int) int {
	if len(prices) == 1{
		return 0
	}
	maxProf := 0
    minPrice := prices[0]
	for _, val := range prices{
		minPrice = min(minPrice, val)
        maxProf = max(maxProf, val-minPrice)
	}
	return maxProf
}
