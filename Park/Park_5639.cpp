#include <iostream>
#include <vector>
using namespace std;

struct Node {
	Node* left;
	Node* right;
	int value;
};

Node* preorder(Node* node, int key) {
	if (node == NULL) {	// NULL 상태의 node에 key값 삽입
		node = new Node();
		node->value = key;
		node->left = NULL;	// 왼쪽 오른쪽 NULL로 초기화해줌.
		node->right = NULL;
	}
	if (node->value > key) {
		node->left = preorder(node->left, key);	// 한 칸씩 점점 내려가면서 key 삽입할 위치 찾아냄
	}
	if (node->value < key) {
		node->right = preorder(node->right, key);	// 한 칸씩 내려가면서 key 삽입할 위치 찾아냄
	}

	return node;
}

void postorder(Node* node) {
	// 왼쪽부터 순차적으로 탐색 시작
	if (node->left != NULL)
		postorder(node->left);
	// 왼쪽 다 했으면 그 다음으로 오른쪽 탐색
	if (node->right != NULL)
		postorder(node->right);
	cout << node->value << "\n";
	// 이미 사용했다는 걸 알려주기 위해 NULL처리했음
	node = NULL;
}

int main() {

	Node* tree = NULL;
	while (true) {	// 종료될 때까지,,,
		int n;
		cin >> n;
		if (cin.eof() == true)	// eof는 ctrl+z
			break;
		tree = preorder(tree, n);	// 입력 즉시 트리에 삽입

	}

	postorder(tree);



	return 0;
}
