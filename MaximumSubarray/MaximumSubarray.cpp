#include<iostream>
#include<vector>
using namespace std;

int maxSubArray(vector<int>& nums) {
	if (nums.size() == 0) return 0;

	int curr_sum = 0;
	int max_sum = INT_MIN;
	for (int i = 0; i < nums.size(); i++) {
		if (curr_sum + nums[i] >= nums[i])
			curr_sum += nums[i];
		else
			curr_sum = nums[i];
		if (max_sum < curr_sum)
			max_sum = curr_sum;
	}
	return max_sum;
}


int main() {
	//vector<int> nums = { -2,1,-3,4,-1,2,1,-5,4 };
	//vector<int> nums = {-2 , 1};
	//vector<int> nums = { -1, 0, -2 };
	//vector<int> nums = { 8, -19, 5, -4, 20 };
	vector<int> nums = {2,0,3,-2};
	cout << maxSubArray(nums) << endl;
	cin.get();
	return 0;
}