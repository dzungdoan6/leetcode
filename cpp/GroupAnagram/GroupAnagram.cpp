#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

void sortString(string &str) {
	sort(str.begin(), str.end());
}
vector<vector<string>> groupAnagrams(vector<string>& strs) {
	vector<vector<string>> result;
	map<string, int> dicts;
	
	int group_idx = 0;
	for (int i = 0; i < strs.size(); i++) {
		string s = strs[i];
		sortString(s);
		map<string, int>::iterator it = dicts.find(s);
		
		// unable to find 
		if (it == dicts.end()) {
			vector<string> group;
			group.push_back(strs[i]);
			result.push_back(group);

			dicts.insert(pair<string, int>(s, group_idx));
			group_idx++;
		}
		else {
			result[it->second].push_back(strs[i]);
		}

	}

	return result;
}
int main() {
	vector<string> strs = { "eat", "tea", "tan", "ate", "nat", "bat" };
	vector<vector<string>> result = groupAnagrams(strs);

	for (int i = 0; i < result.size(); i++) {
		vector<string> group = result[i];
		for (int k = 0; k < group.size(); k++)
			cout << group[k] << ", ";
		cout << endl;
	}

	
	cin.get();
	return -1;
}