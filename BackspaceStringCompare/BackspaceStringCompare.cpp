#include<iostream>
#include<string>
using namespace std;

void makeFinalString(string &S, int &idx_end) {
	idx_end = -1;
	for (int i = 0; i < S.length(); i++) {
		if (S[i] != '#') {
			S[idx_end + 1] = S[i];
			idx_end++;
			continue;
		}

		if (S[i] == '#' && idx_end >= 0)
			idx_end--;
	}
}
bool backspaceCompare(string S, string T) {
	int s_idx;
	makeFinalString(S, s_idx);
	int t_idx;
	makeFinalString(T, t_idx);

	if (s_idx == -1 && t_idx == -1) return true;
	if (s_idx != t_idx)  return false;

	return S.substr(0, s_idx + 1).compare(T.substr(0, t_idx + 1)) == 0;
}

int main() {
	
	cout << backspaceCompare("ab#c", "ad#c") << endl;
	cout << backspaceCompare("ab##", "c#d#") << endl;
	cout << backspaceCompare("a##c", "#a#c") << endl;
	cout << backspaceCompare("a#c", "b") << endl;
	cout << backspaceCompare("y#fo##f", "y#f#o##f") << endl;
	cin.get();
	return 1;
}