#include <iostream>
#include <algorithm>
using namespace std;

typedef struct _node {
	_node* left;
	_node* right;
	int val;
}node;

node* t, *head;

void preorder(int key, node* head) {
	if (head->val > key)
		if (head->left != NULL)
			preorder(key, head->left);
		else {
			t = (node*)calloc(1, sizeof(node));
			t->left = t->right = NULL;
			t->val = key;
			head->left = t;
		}
	else
		if (head->right != NULL)
			preorder(key, head->right);
		else {
			t = (node*)calloc(1, sizeof(node));
			t->left = t->right = NULL;
			t->val = key;
			head->right = t;
		}
}

void postorder(node* head) {
	if (head->left != NULL)
		postorder(head->left);
	if (head->right != NULL)
		postorder(head->right);
	cout << head->val << endl;
}

int main() {
	int key;
	head = (node*)calloc(1, sizeof(node));
	head->left = head->right = NULL;
	head->val = 1000001;

	while (1) {
		cin >> key;
		if (cin.eof()) break;
		preorder(key, head);
	}
	postorder(head->left);
}