#include <iostream>
#include <vector>
using namespace std;

int maxProfit(vector<int>& prices) 
{
	if (prices.size() == 0)
		return 0;
	int profit = 0;
	int p1, p2;
	p1 = 0;
	p2 = 1;
	while (p2 < prices.size())
	{
		if (prices[p2] < prices[p2 - 1])
		{
			profit = profit + (prices[p2 - 1] - prices[p1]);
			p1 = p2;
			p2 = p1 + 1;
		}
		else
			p2++;
	}
	profit = profit + prices[p2-1] - prices[p1];
	return profit;
}

int main()
{
	vector<int> prices = { };
	int max_profit = maxProfit(prices);
	cout << max_profit << endl;
	cin.get();
	return 1;
}