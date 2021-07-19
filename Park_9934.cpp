#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

vector<int> inorder;
vector<vector<int>> ans(10);	// 최종 결과. 최대가 10이니깐 10으로 벡터 만듦

void getTree(int level, int left, int right) {
	if (left >= right) {	// 종료 조건
		ans[level].push_back(inorder[left]);
		return;
	}
	
	// 중위 순회에서 루트는 가운데에 있는 거더라
	int mid = (left + right) / 2;
	ans[level].push_back(inorder[mid]);
	getTree(level+1, left, mid - 1);	// 왼쪽 탐색
	getTree(level+1, mid + 1, right);	// 오른쪽 탐색
}

int main() {

	int K;
	cin >> K;

	int max = pow(2, K)-1;

	for (int i = 0; i < max; i++) {
		int N;
		cin >> N;
		inorder.push_back(N);
	}

	getTree(0, 0, max - 1);	// index는 0부터 시작해서 최대가 max-1

	for (int i = 0; i < K; i++) {
		for (int j = 0; j < ans[i].size(); j++) {
			cout << ans[i][j] << " ";
		}
		cout << "\n";
	}

	return 0;
}
