class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;
        for(let i = 0; i< prices.length; i++){
            if(i===0) continue;
            const profit = prices[i]-prices[i-1];
            maxProfit += Math.max(0, profit);
        }
        return maxProfit;
    }
}
