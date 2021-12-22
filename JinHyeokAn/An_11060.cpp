#include <iostream>
using namespace std;

#define INF 9999999
int num[1001] = { 0, }, result[1001] = { 0, };

int main() {
	int N, M;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> M;
		num[i] = M;
		result[i] = INF;
	}
	result[0] = 0;
	for (int i = 0; i < N; i++) for (int j = i + 1; j <= i + num[i]; j++) if(result[j] > result[i] + 1) result[j] = result[i] + 1;
	if (result[N - 1] == INF) cout << -1;
	else cout << result[N - 1];
}