//14888. 연산자 끼워넣기
#include <iostream>
#include <algorithm>
using namespace std;
#define MAX 100000000
int N;
int A[12] = { 0 };
int op[4] = { 0 };
int m, M; //max,min

void DFS(int plus, int minus, int multiply, int divide, int count, int result) {
	if (count == N) {
		if (m < result) {
			m = result;
		}
		if (M > result) {
			M = result;
		}
		return;
	}
	
	if (plus > 0) {
		DFS(plus-1, minus, multiply, divide, count+1, result + A[count]);
	}
	if (minus > 0) {
		DFS(plus, minus-1, multiply, divide, count + 1, result - A[count]);
	}
	if (multiply > 0) {
		DFS(plus, minus, multiply-1, divide, count + 1, result * A[count]);
	}
	if (divide > 0) {
		DFS(plus, minus, multiply, divide-1, count + 1, result / A[count]);
	}

}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < 4; i++) {
		cin >> op[i];
	}
	m = -MAX;
	M = MAX;

	DFS(op[0], op[1], op[2], op[3], 1, A[0]);

	cout << m << " " << M << " ";
	return 0;
}