#include <iostream>
#include <algorithm>
using namespace std;

typedef struct code {
	int x, y, z;
}cd;

cd store[101];

bool cmp(const cd& a, const cd& b) {
	return a.z < b.z;
}

int main() {
	int N, K, x, y, z, cnt, ans = 99999999;
	cin >> N >> K;
	cd t;
	for (int i = 0; i < N; i++) {
		cin >> x >> y >> z;
		t.x = x; t.y = y; t.z = z;
		store[i] = t;
	}
	sort(store, store + N, cmp);

	for (int i = 0; i < N; i++) {
		x = store[i].x;
		for (int j = 0; j < N; j++) {
			y = store[j].y;
			cnt = 0;
			for (int k = 0; k < N; k++) {
				if (store[k].x <= x && store[k].y <= y) {
					cnt++;
					z = store[k].z;
				}
				if (cnt == K) break;
			}
			if (cnt == K)
				ans = min(ans, x + y + z);
		}
	}
	cout << ans;
}