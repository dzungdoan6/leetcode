#include<iostream>
#include<unordered_set>
using namespace std;

int sumSquare(int n) {
	int sum = 0;
	while (n != 0) {
		int remainder = n % 10;
		n /= 10;
		sum += remainder * remainder;
	}
	return sum;
}

bool isHappy(int n) {

	unordered_set<int> check;
	unordered_set<int>::iterator it = check.end();
	while (it == check.end()) {
		int sum = sumSquare(n);
		if (sum == 1)
			return true;
		it = check.find(sum);
		if (it != check.end())
			return false;
		check.insert(sum);
		n = sum;
	}
	return false;
}


int main() {
	int num = 19;

	cout << isHappy(num) << endl;
	cin.get();
	return 1;

}
