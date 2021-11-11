#include <iostream>
#include <cstdlib>
#include <queue>
using namespace std;

typedef struct _class {
	int time;
	int flag;
}cla;

cla store[202000];

struct cmp {
	bool operator()(const cla& t, const cla& u) {
		return t.time > u.time;
	}
};

int main() {
	priority_queue<cla, vector<cla>, cmp> q;
	int count, number, start, end, num = 0, sum = 0, max = 0, flag = 1;
	cin >> count;
	for (int i = 0; i < count; i++) {
		cin >> number >> start >> end;
		store[i * 2].time = start;
		store[i * 2].flag = 1;
		store[i * 2 + 1].time = end;
		store[i * 2 + 1].flag = -1;
	}
	for (int i = 0; i < count * 2; i++)
		q.push(store[i]);

	while (1) {
		cla a, b;
		a = q.top();
		q.pop();
		b = q.top();
		q.pop();
		while (a.time == b.time) {
			sum += a.flag;
			if (q.empty()) {
				flag = 0;
				break;
			}
			q.push(b);
			a = q.top();
			q.pop();
			b = q.top();
			q.pop();
		}
		if(flag == 1)
			sum += a.flag;
		if (sum > max)
			max = sum;
		if (q.empty())
			break;
		q.push(b);
	}
	cout << max;
}