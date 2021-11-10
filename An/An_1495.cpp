#include <iostream>
using namespace std;

int num[101];
bool vol[101][1001];

int main() {
	int n, s, max, res = -1;
	cin >> n >> s >> max;
	for (int i = 1; i <= n; i++) cin >> num[i];
	vol[0][s] = true;
	for (int i = 0; i < n; i++) {
		int val = num[i + 1];
		for (int j = max; j >= 0; j--) {
			if (vol[i][j]) {
				if (j + val <= max) vol[i + 1][j + val] = true;
				if (j - val >= 0) vol[i + 1][j - val] = true;
			}
		}
	}
	for (int i = max; i >= 0; i--) {
		if (vol[n][i] == true) {
			res = i;
			break;
		}
	}
	cout << res;
}