#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// 내가 직접 지정한 비교함수
bool comp(pair<int, int> a, pair<int, int> b) {
	return a.second > b.second;
}

int main() {

	int N;
	cin >> N;

	vector<int> arr1;
	vector<pair<int, int>> arr2;
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		arr1.push_back(temp);
	}
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		arr2.push_back(make_pair(i + 1, temp));
	}

	sort(arr2.begin(), arr2.end(), comp);
	sort(arr1.begin(), arr1.end());

	int res = 0;
	for (int i = 0; i < N; i++) {
		res += arr2[i].second * arr1[i];
	}

	cout << res;

	return 0;
}
