#include<iostream>
#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;

int lastStoneWeight(vector<int>& stones) {
	make_heap(stones.begin(), stones.end());

	while (stones.size() > 1) {
		int st1 = stones.front();
		pop_heap(stones.begin(), stones.end());
		stones.pop_back();

		int st2 = stones.front();
		pop_heap(stones.begin(), stones.end());
		stones.pop_back();

		int remain = abs(st1 - st2);
		if (remain > 0) {
			stones.push_back(remain);
			push_heap(stones.begin(), stones.end());
		}
	}

	if (stones.size() == 0)
		return 0;
	return stones[0];
}


int main() {
	//vector<int> stones = { 2,7,4,1,8,1 };
	vector<int> stones = { 7,7,6,6,9 };
	cout << lastStoneWeight(stones) << endl;
	cin.get();
	return 1;
}