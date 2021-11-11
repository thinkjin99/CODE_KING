#include <iostream>
using namespace std;

int box[1001] = { 0, };
int res[1001];

int main() {
	int N, num, max = 0;
	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> box[i];
		res[i] = 1;
	}
	for (int i = 1; i < N; i++) for (int j = i + 1; j <= N; j++) if (box[j] > box[i]) if (res[j] < res[i] + 1) res[j] = res[i] + 1;
	for (int i = 1; i <= N; i++) if (max < res[i]) max = res[i];
	cout << max;
}