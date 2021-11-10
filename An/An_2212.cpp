#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int sen[10100];

bool compare(int a, int b) {
	return a < b;
}

int main() {
	int s_cnt, g_cnt, number, max;
	cin >> s_cnt;
	cin >> g_cnt;
	priority_queue<int> pq_l;
	if (s_cnt < g_cnt)
		g_cnt = s_cnt;
	
	for (int i = 0; i < s_cnt; i++) {
		cin >> number;
		sen[i] = number;
	}

	sort(sen, sen + s_cnt, compare);

	for (int j = 0; j < s_cnt - 1; j++)
		pq_l.push(abs(sen[j + 1] - sen[j]));
	max = sen[s_cnt - 1] - sen[0];
	for (int k = 1; k < g_cnt; k++) {
		max -= pq_l.top();
		pq_l.pop();
	}
	cout << max;
}