class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        currentSum = prices[1] - prices[0]
        first = prices[0]
        maxProfit = 0
        for price in prices:
            currentSum = price - first
            if currentSum < 0:
                currentSum = 0
                first = price
            maxProfit = max(maxProfit, currentSum)

        return maxProfit
