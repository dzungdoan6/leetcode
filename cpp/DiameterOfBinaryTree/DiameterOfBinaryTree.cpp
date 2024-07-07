#include<iostream>
#include<vector>
using namespace std;

struct TreeNode {
	int val;
	TreeNode* left;
	TreeNode* right;
	TreeNode(int x): val(x), left(NULL), right(NULL) {}
};

int treeDepth(TreeNode* root) {
	if (root == NULL)
		return 0;
	int left_depth = treeDepth(root->left);
	int right_depth = treeDepth(root->right);
	if (left_depth > right_depth)
		return left_depth + 1;
	return right_depth + 1;
}

int computeDiameter(TreeNode* root) {
	if (root == NULL) return 0;

	int left_depth = treeDepth(root->left);
	int left_right = treeDepth(root->right);
	return left_depth + left_right + 1;
}

void computeAllDiameters(TreeNode* root, vector<int> &diameters) {
	if (root == NULL)
		return;
	int dia = computeDiameter(root);
	diameters.push_back(dia);

	if (root->left != NULL) {
		computeAllDiameters(root->left, diameters);
	}

	if (root->right != NULL) {
		computeAllDiameters(root->right, diameters);
	}
}

int diameterOfBinaryTree(TreeNode* root) {
	if (root == NULL) return 0;

	vector<int> diameters;
	computeAllDiameters(root, diameters);

	int max_dia = INT_MIN;
	for (int i = 0; i < diameters.size(); i++)
		if (diameters[i] > max_dia)
			max_dia = diameters[i];
	return max_dia;
}

int main() {
	TreeNode* root = new TreeNode(1);
	root->left = new TreeNode(2);
	root->right = new TreeNode(3);
	
	
	root->left->left = new TreeNode(4);
	root->left->left->right = new TreeNode(10);
	
	root->left->right = new TreeNode(5);
	root->left->right->right = new TreeNode(6);
	root->left->right->right->left = new TreeNode(7);
	root->left->right->right->left->left = new TreeNode(20);
	root->left->right->right->left->right = new TreeNode(8);
	
	cout << diameterOfBinaryTree(root) << endl;
	
	cin.get();
	return 1;
}