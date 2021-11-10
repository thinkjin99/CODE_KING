#include <iostream>
using namespace std;

int num[100] = { 0, };

int main() {
	int N, M, A, B, F, S, cnt = 1;
	num[1] = 1;  num[2] = 1; num[3] = 2;
	for (int i = 4; i < 30; i++) num[i] = num[i - 1] + num[i - 2];
	cin >> N >> M;
	A = num[N - 2]; B = num[N - 1];
	while (1) {
		if (!((M - B * cnt) % A)) {
			F = (M - B * cnt) / A;
			S = cnt;
			if (F < S) break;
			else cnt++;
		}
		else cnt++;
	}
	cout << F << "\n" << S;
}