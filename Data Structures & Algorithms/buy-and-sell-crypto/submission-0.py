class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        maxSell = 0
        for i in prices[::-1]:
            currProfit = maxSell - i
            maxDiff = max(maxDiff, currProfit)
            maxSell = max(maxSell, i)
        return maxDiff