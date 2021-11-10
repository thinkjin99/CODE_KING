#include <iostream>
#include <algorithm>
using namespace std;

int home[200000];

int find(int home_cnt, int gong_cnt) {
	int left = 1, right = home[home_cnt - 1] - home[0], result;
	while (left <= right) {
		int cnt = 1, start = home[0], mid = (left + right) / 2;
		for (int i = 1; i < home_cnt; i++) {
			int dis = home[i] - start;
			if (dis >= mid) {
				cnt++;
				start = home[i];
			}
		}
		if (cnt >= gong_cnt) {
			result = mid;
			left = mid + 1;
		}
		else
			right = mid - 1;
	}
	return result;
}

int main() {
	int home_cnt, gong_cnt, result;
	cin >> home_cnt >> gong_cnt;
	for (int i = 0; i < home_cnt; i++)
		cin >> home[i];
	sort(home, home + home_cnt);
	result = find(home_cnt, gong_cnt);
	cout << result;
}