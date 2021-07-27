#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N, M;
	cin >> N >> M;

	map<string, string> m;

	for (int i = 0; i < N; i++) {
		string link, pw;
		cin >> link >> pw;

		m[link] = pw;
	}

	for (int i = 0; i < M; i++) {
		string link;
		cin >> link;

		cout << m[link] << "\n";
	}

	return 0;
}
