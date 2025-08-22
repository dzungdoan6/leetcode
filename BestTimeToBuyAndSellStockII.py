from typing import List
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    current_profit = 0
    current_smallest = prices[0]
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            current_profit = prices[i] - current_smallest
        else:
            max_profit += current_profit
            current_profit = 0
            current_smallest = prices[i]
    max_profit += current_profit
    return max_profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))

prices = [1,2,3,4,5]
print(maxProfit(prices))


prices = [7,6,4,3,1]
print(maxProfit(prices))
