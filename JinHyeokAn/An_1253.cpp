#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int num, val, result = 0;
	int arr[2010];
	cin >> num;
	for (int i = 0; i < num; i++)
		cin >> arr[i];
	sort(arr, arr + num);

	for (int i = 0; i < num; i++) {
		val = arr[i];
		int l = 0, r = num - 1, sum;
		while (l < r) {
			sum = arr[l] + arr[r];
			if (sum == val) {
				if (l != i && r != i) {
					result++;
					break;
				}
				else if (l == i) l++;
				else if (r == i) r--;
			}
			else if (sum < val) l++;
			else r--;
		}
	}
	cout << result;
}