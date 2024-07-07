#include<iostream>
#include<unordered_set>
#include<vector>
using namespace std;


int singleNumber(vector<int>& nums)
{
	unordered_set<int> set;
	unordered_set<int>::iterator it;
	for (int i = 0; i < nums.size(); i++)
	{
		it = set.find(nums[i]);
		if (it == set.end())
			set.insert(nums[i]);
		else
			set.erase(it);
	}
	return *set.begin();
}

int main()
{
	vector<int> nums = { 2,2,1 };
	cout << singleNumber(nums) << endl;
	cin.get();
	return 1;
}