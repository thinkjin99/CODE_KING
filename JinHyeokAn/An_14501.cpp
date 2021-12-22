#include <iostream>
using namespace std;

int Ti[20], Pi[20], res[20] = { 0, };

int main() {
	int N, max = 0;
	cin >> N;
	for (int i = 1; i <= N; i++) cin >> Ti[i] >> Pi[i];
	for (int i = 1; i <= N; i++) if (i + Ti[i] - 1 <= N) for(int j = i + Ti[i]; j <= N + 1; j++) if(res[j] < Pi[i] + res[i]) res[j] = Pi[i] + res[i];
	for (int i = 1; i <= N + 1; i++) if (max < res[i]) max = res[i];
	cout << max;
}