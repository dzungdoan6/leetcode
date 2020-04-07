#include<iostream>
#include<vector>
#include<algorithm>
#include<unordered_set>
using namespace std;


int countElements(vector<int>& arr) {
	int count = 0;
	sort(arr.begin(), arr.end());
	std::unordered_set<int> dict; // pair <array value-number of occurences>
	std::unordered_set<int>::iterator it_current;
	std::unordered_set<int>::iterator it_prev;

	for (int i = arr.size()-1; i >= 0; i--) {
		it_current = dict.find(arr[i]); // search x value
		it_prev = dict.find(arr[i]+1); // search x-1 value

		// insert if x doesn't exist
		if (it_current == dict.end()) 
			dict.insert(arr[i]); 

		// if x-1 value exists, increase count
		if (it_prev != dict.end()) count++;
		
	}
	return count;
}
int main() {
	vector<int> arr = { 1,2,3 };
	//vector<int> arr = { 1,1,3,3,5,5,7,7 };
	//vector<int> arr = { 1,3,2,3,5,0 };
	//vector<int> arr = { 1,1,2,2 };
	//vector<int> arr = {1, 1, 2};
	cout << countElements(arr) << endl;
	cin.get();
	return 1;
}