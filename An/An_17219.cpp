#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
#include <map>
using namespace std;

map<string, string> m;

int main() {
	cin.tie(NULL);
	ios::sync_with_stdio(false);
	int N, M;
	string si, pa;
	cin >> N >> M;
	for (int i = 0; i < N; i++) {
		cin >> si >> pa;
		m[si] = pa;
	}
	for (int j = 0; j < M; j++) {
		cin >> si;
		cout << m[si] << "\n";
	}
}