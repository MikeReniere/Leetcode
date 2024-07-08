from typing import List
class Solution:
    def maxProfit(prices: List[int]) -> int:
        l, r = 0, 1 #left buy, right sell
        maxP = 0

        while r < len(prices):
            #is it profitable
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else: # non profitable
                l = r #move l to equal r, then move r + 1 
            r += 1
        return maxP

    prices = [7,1,5,3,6,4]
    print(maxProfit(prices))