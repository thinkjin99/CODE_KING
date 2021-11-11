#include <iostream>
#include <string>
#include <map>
#include <cmath>
using namespace std;

//vector<pair<string, double>> ans;
map<string, float> ans; //원래 이차원 백터로 만들려고 했는데 map사용

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios::sync_with_stdio(false);
	string t;

	float cnt = 0;

//	for (int i = 0; i < max; i++) {
//		cin >> t;
//		tree.push_back(t);
//		cnt++;
//	}
	
	while (getline(cin, t)) {
		if (ans.find(t) == ans.end()) {
			ans[t] = 1;
		}
		else {
			++ans[t]; //해당 나무 그루 수 1 증가
		}
		++cnt; //전체 나무 수 1 증가
	}

	cout << fixed; 
	cout.precision(4); //소수점 아래 넷째자리까지만 표현하도록 고정

	for (auto it = ans.begin(); it != ans.end(); it++) { //맵 전체 원소 출력
		float val = (it->second / cnt) * 100;
		cout << it->first << ' ' ;
		cout << val << "\n";
	}
	
	return 0;
}