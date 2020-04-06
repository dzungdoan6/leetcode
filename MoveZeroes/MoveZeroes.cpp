#include<iostream>
#include<vector>
using namespace std;

void moveZeroes(vector<int>& nums)
{
	int k = 0;
	while (k < nums.size() && nums[k] != 0 )
		k++;

	for (int i = k+1; i < nums.size(); i++)
	{
		if (nums[i] != 0)
		{
			nums[k] = nums[i];
			nums[i] = 0;
			k++;
		}
	}
}

int main()
{
	vector<int> nums = { 1};
	moveZeroes(nums);
	for (int i = 0; i < nums.size(); i++)
		cout << nums[i] << endl;
	cin.get();
	return 1;
}