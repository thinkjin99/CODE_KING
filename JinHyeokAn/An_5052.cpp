#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

int main() {
	int case_num, add_num;
	cin >> case_num;

	vector<string> pvec;

	while(case_num--){
		bool flag = 1;
		cin >> add_num;
		for (int j = 0; j < add_num; j++) {
			string ph_num;
			cin >> ph_num;
			pvec.push_back(ph_num);
		}
		sort(pvec.begin(), pvec.end());
		for (int k = 0; k < pvec.size() - 2; k++) {
			int a = pvec[k].length(), b = pvec[k + 1].length();
			if (a == b) continue;
			if (pvec[k + 1].substr(0, a) == pvec[k]) {
				flag = 0;
				cout << "NO" << endl;
				break;
			}
		}
		if (flag == 1) cout << "YES" << endl;
		pvec.clear();
	}
}