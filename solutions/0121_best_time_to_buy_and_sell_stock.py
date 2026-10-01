class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxx = 0
        buyprice = float("inf")
        for i in range(len(prices)):
            if buyprice < prices[i]:
                profit = prices[i]-buyprice
                maxx = max(maxx,profit)
            else:
                buyprice = prices[i]
        return maxx
