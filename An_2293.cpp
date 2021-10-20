#include <iostream>
using namespace std;

int coin[101] = { 0, }, num[10001] = { 0, };

int main() {
	int N, M, cost;
	cin >> N >> M;
	for (int i = 1; i <= N; i++) {
		cin >> coin[i];
	}
	num[0] = 1;
	for (int i = 1; i <= N; i++) {
		for (int j = coin[i]; j <= M; j++) {
			num[j] += num[j - coin[i]];
		}
	}
	cout << num[M];
}