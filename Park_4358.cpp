#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <cstdio>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	map<string, double> m;
	int cnt = 0;

	string str;

	while (getline(cin, str)) {
		if (str == "\n")
			break;
		m[str]++;
		cnt++;
	}

	cout << fixed;
	cout.precision(4);

	for (auto it = m.begin(); it != m.end(); it++)
		cout << it->first << " " << (it->second)/cnt * 100 << "\n";

	/*for (int i = 0; i < v.size(); i++) {
		cout << v[i].first;
		printf(" %.4f\n",v[i].second / cnt * 100);
	}*/
	
	

	return 0;
}
