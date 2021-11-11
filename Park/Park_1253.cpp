#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	vector<int> v;
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;
		v.push_back(num);
	}

	sort(v.begin(), v.end());

	int cnt = 0;
	for (int i = 0; i < N; i++) {
		int key = v[i];
		
		int left = 0, right = N - 1;	// 왼쪽이랑 오른쪽 해서 투포인터?로 진행
		while (left < right) {	// 종료 조건
			// 본인은 빼고 계산해야 되므로,,,~
			if (left == i) {
				left++;
				continue;
			}
			if (right == i) {
				right--;
				continue;
			}

			int sum = v[left] + v[right];
			if (sum == key) {
				cnt++;
				break;
			}

			// index 옮기기
			if (sum > key)
				right--;
			else
				left++;
		}
	}

	cout << cnt;

	return 0;
}
