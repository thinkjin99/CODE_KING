#include <iostream>
using namespace std;

int res[100001];

int main() {
	int N;
	cin >> N;
	res[1] = 3; res[2] = 7;
	for (int i = 3; i <= N; i++) res[i] = (res[i - 1] * 2) % 9901 + res[i - 2] % 9901;
	cout << res[N] % 9901;
}