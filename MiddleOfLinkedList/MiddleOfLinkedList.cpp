#include<iostream>
#include<vector>
using namespace std;

struct ListNode {
	int val;
	ListNode* next;
	ListNode(int x) : val(x), next(NULL) {}
};

// Use fast and slow pointers, where fast traverses two times faster than slow
// Complexity O(n)
ListNode* middleNode(ListNode* head) {
	if (head == NULL) return NULL;
	ListNode* slow = head;
	ListNode* fast = head;
	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}
	return slow;
}

int main() {
	// create a simple linked list
	ListNode* head = new ListNode(1);
	ListNode* p = head;
	for (int i = 2; i <= 6; i++) {
		p->next = new ListNode(i);
		p = p->next;
	}

	// solve the problem
	ListNode* middle = middleNode(head);
	cout << middle->val << endl;
	cin.get();
	return 1;
}