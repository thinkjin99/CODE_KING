#include <iostream>

using namespace std;

int main() {
	int N, K, s = 0;
	cin >> N >> K;
	int* number, * visit;
	number = (int*)calloc(N + 1, sizeof(int));
	visit = (int*)calloc(N + 1, sizeof(int));

	for (int i = 1; i <= N; i++) number[i] = i;
	cout << "<";
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < K; j++) {
			s++;
			if (s > N) s = 1;
			if (visit[s] == 1) {
				while (1) {
					if (visit[s] == 0) break;
					s++;
					if (s > N) s = 1;
				}
			}
		}
		visit[s] = 1;
		if (i == N - 1) cout << number[s] << ">";
		else cout << number[s] << ", ";
	}
}