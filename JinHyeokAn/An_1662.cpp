#include <iostream>
using namespace std;

int ch2in(char c) {
	return c - '0';
}

int visit[51] = { 0, };

int recur(string& str, int num) {
	int cnt = 0;
	for (int i = num; i < str.size(); i++) {
		if (!visit[i]) {
			visit[i] = 1;
			if (str[i] == '(') cnt += ch2in(str[i - 1]) * recur(str, i + 1) - 1;
			else if (str[i] == ')') return cnt;
			else cnt++;
		}
	}
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string str;
	cin >> str;
	cout << recur(str, 0);
}