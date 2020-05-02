
// Sample code to perform I/O:

#include <iostream>

using namespace std;

struct node {
	int data;
	struct node *left;
	struct node *right;
};

int resultLength = 0;

int maxDepth(struct node *ptr) {
	int leftCount = 0, rightCount = 0;
	if (ptr -> left != NULL) {
		leftCount = maxDepth(ptr -> left);
	}
	if (ptr -> right != NULL) {
		rightCount = maxDepth(ptr -> right);
	}
	resultLength = max(leftCount + rightCount + 1, resultLength);
	return max(leftCount, rightCount) + 1;
}

int main() {
	int n, x;
	struct node *root;
	string pos;
	cin >> n >> x;
	root = new struct node;
	root -> data = x;
	while (--n) {
		struct node *ptr = root;
		cin >> pos;
		for (int i = 0; i < pos.length(); i++) {
			if (pos[i] == 'L') {
				if (ptr -> left == NULL) {
					ptr -> left = new struct node;
				}
				ptr = ptr -> left;
			} else if (pos[i] == 'R') {
				if (ptr -> right == NULL) {
					ptr -> right = new struct node;
				}
				ptr = ptr -> right;
			}
		}
		cin >> ptr -> data;
	}
	maxDepth(root);
	cout << resultLength;
	return 0;
}