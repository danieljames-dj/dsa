#include <iostream>
#include <string>

using namespace std;

struct node {
	int data;
	struct node *left;
	struct node *right;
};

int insert(struct node *ptr, int par, int ch, char pos) {
	if (ptr -> data == par) {
		if (pos == 'L') {
			ptr -> left = new struct node;
			ptr -> left -> data = ch;
		} else {
			ptr -> right = new struct node;
			ptr -> right -> data = ch;
		}
		return 1;
	} else {
		int inserted = 0;
		if (ptr -> left) {
			inserted = insert(ptr -> left, par, ch, pos);
		}
		if (!inserted && ptr -> right) {
			inserted = insert(ptr -> right, par, ch, pos);
		}
		return inserted;
	}
}

string getPosition(struct node *ptr, int data, string curPos) {
	if (ptr -> data == data) {
		return curPos;
	} else {
		string pos;
		if (ptr -> left) {
			pos = getPosition(ptr -> left, data, curPos + "L");
		}
		if (pos == "" && ptr -> right) {
			pos = getPosition(ptr -> right, data, curPos + "R");
		}
		return pos;
	}
}

int main() {
	int n, q, par, ch;
	char pos;
	struct node *root = new struct node;
	root -> data = 1;
	cin >> n >> q;
	while (--n) {
		cin >> par >> ch >> pos;
		insert(root, par, ch, pos);
	}
	while (q--) {
		int el;
		cin >> el;
		string pos = getPosition(root, el, "X");
		if (pos != "") {
			struct node *ptr = root;
			for (int i = 1; ptr && (i < pos.length()); i++) {
				if (pos[i] == 'L') {
					ptr = ptr -> right;
				} else {
					ptr = ptr -> left;
				}
			}
			if (ptr) {
				cout << ptr -> data << endl;
			} else {
				cout << "-1" << endl;
			}
		} else {
			cout << "-1" << endl;
		}
	}
	return 0;
}
