#include<stack>;
#include<iostream>;
using namespace std;


class MinStack {
private:
	stack<int> st;
	
public:
	MinStack() {
		st = stack<int>();
	}
	void push(int x) {
		if (st.empty()) {
			st.push(x);
			st.push(x);
		}
		else {
			int min = (x < getMin()) ? x : getMin();
			st.push(x);
			st.push(min);
		}	
	}

	void pop() {
		st.pop();
		st.pop();
	}

	int top() {
		int min = st.top();
		st.pop();
		int val = st.top();
		st.push(min);
		return val;
	}

	int getMin() {
		return st.top();
	}
};
int main() {
	MinStack* minStack = new MinStack();
	minStack->push(-2);
	minStack->push(0);
	minStack->push(-3);
	cout << minStack->getMin() << endl;
	minStack->pop();
	cout << minStack->top() << endl;
	cout << minStack->getMin() << endl;
	cin.get();
	return 1;
}