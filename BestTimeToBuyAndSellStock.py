from typing import List
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    curr_lowest = prices[0]
    n = len(prices)
    for i in range(n):
        if prices[i] - curr_lowest > max_profit:
            max_profit = prices[i] - curr_lowest
        if prices[i] < curr_lowest:
            curr_lowest = prices[i]
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices=prices))

prices = [7,6,4,3,1]
print(maxProfit(prices=prices))