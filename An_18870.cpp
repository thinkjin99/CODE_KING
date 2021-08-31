#include <iostream>
#include <queue>
using namespace std;

struct cd {
	int x, idx;
	cd(int x, int idx): x(x), idx(idx){}
};

struct cmp {
	bool operator()(cd a, cd b) {
		return a.x > b.x;
	}
};

int code[1000001];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, num, count = -1, pre = 1000001, pre_cnt = 0;
	priority_queue<cd, vector<cd>, cmp> pq;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> num;
		pq.push(cd(num, i));
	}
	for (int i = 0; i < N; i++) {
		if (pre != pq.top().x)
			code[pq.top().idx] = ++count;
		else
			code[pq.top().idx] = count;
		pre = pq.top().x;
		pq.pop();
	}
	for (int i = 0; i < N; i++)
		cout << code[i] << " ";
}