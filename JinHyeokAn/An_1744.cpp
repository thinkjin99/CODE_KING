#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int pl[10100];
int mi[10100];
int zero[10100];
int one[10100];

bool compare_up(int a, int b) {
	return a < b;
}

bool compare_down(int a, int b) {
	return a > b;
}

int main() {
	int cnt, number, m = 0, p = 0, z = 0, sum = 0, o = 0;
	cin >> cnt;
	for (int i = 0; i < cnt; i++) {
		cin >> number;
		if (number < 0)
			mi[m++] = number;
		else if (number > 1)
			pl[p++] = number;
		else if (number == 0)
			zero[z++] = number;
		else if (number == 1)
			one[o++] = number;
	}
	sort(pl, pl + p, compare_down);
	sort(mi, mi + m, compare_up);

	if (p % 2 == 0) {
		for (int i = 0; i < p / 2; i++)
			sum += pl[i * 2] * pl[i * 2 + 1];
	}
	else if (p % 2 == 1) {
		for (int i = 0; i < (p - 1) / 2; i++)
			sum += pl[i * 2] * pl[i * 2 + 1];
		sum += pl[p - 1];
	}

	if (m % 2 == 0) {
		for (int i = 0; i < m / 2; i++)
			sum += mi[i * 2] * mi[i * 2 + 1];
	}
	else if (m % 2 == 1) {
		for (int i = 0; i < (m - 1) / 2; i++)
			sum += mi[i * 2] * mi[i * 2 + 1];
		if (z > 0)
			sum += 0;
		else if (z == 0)
			sum += mi[m - 1];
	}

	sum += o;

	cout << sum;
}