#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, num;
	long long a = 0, b = 0, sum = 0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		priority_queue<long long, vector<long long>, greater<long long>> pq;
		cin >> M;
		for (int j = 0; j < M; j++) {
			cin >> num;
			pq.push(num);
		}
		sum = 0;
		while (pq.size() >= 2) {
			a = pq.top();
			pq.pop();
			b = pq.top();;
			pq.pop();
			sum += a + b;
			pq.push(a + b);
		}
		pq.pop();
		cout << sum << "\n";
	}
}