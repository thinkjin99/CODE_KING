#include <iostream>
#include <vector>
using namespace std;

vector<int> inOrder, postOrder, res;
int indexArr[100001] = { 0, };

//int getIndex(vector<int> v, int key) {
//	int i;
//	for (i = 0; i < v.size(); i++) {
//		if (v[i] == key)
//			break;
//	}
//	return i;
//}

void getPre(int inLeft, int inRight, int postLeft, int postRight) {
	if (inLeft <= inRight && postLeft <= postRight) {
		res.push_back(postOrder[postRight]);

		/*int inIndex = getIndex(inOrder, postOrder[postRight]);*/
		int inIndex = indexArr[postOrder[postRight]];	// index 단 번에 찾아내버리기 ㅠㅠ
		int leftLen = inIndex - inLeft;	// 범위의 크기?는 항상 똑같아야 하므로~ 이 값 새로 정의
		
		getPre(inLeft, inIndex - 1, postLeft, postLeft + leftLen - 1);
		getPre(inIndex + 1, inRight, postLeft + leftLen, postRight - 1);
	}
	return;
}

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N, num;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> num;
		inOrder.push_back(num);
		indexArr[num] = i;	// index 찾을 때 도움 되도록 하는,,, 배열
	}
	for (int i = 0; i < N; i++) {
		cin >> num;
		postOrder.push_back(num);
	}

	getPre(0, N-1, 0, N-1);

	for (int i = 0; i < N; i++)
		cout << res[i] << " ";

	return 0;
}
