//2293. µ¿Àü1
#include <iostream>
using namespace std;
int c[101];
int DP[10010];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	int n, k;
	cin >> n >> k;

	for (int i = 0; i < n; i++) {
		cin >> c[i];
	}
	DP[0] = 1;
	for (int i = 0; i < n; i++) {
		for (int j = c[i]; j <= k; j++) {
			DP[j] = DP[j] + DP[j - c[i]];
		}
	}
	cout << DP[k] << endl;


	return 0;
}