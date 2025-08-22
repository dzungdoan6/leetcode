from typing import List
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    smallest = prices[0]
    for i in range(1, len(prices)):
        if prices[i] - smallest > max_profit:
            max_profit = prices[i] - smallest
        if prices[i] < smallest:
            smallest = prices[i]

    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [7,6,4,3,1]
print(maxProfit(prices))
