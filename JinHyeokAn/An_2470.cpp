#include <iostream>
#include <algorithm>
using namespace std;

int num[100001], result = 2000000000, one, two, flag = 0;

void binary_search(int number, int size) {
	int left = 0, right = size - 1;
	while (left <= right) {
		int mid = (left + right) / 2;
		if (num[mid] > number) right = mid - 1;
		else if (num[mid] < number) left = mid + 1;
		else {
			one = -number;
			two = number;
			flag = 1;
			break;
		}
	}
	if (flag == 0) {
		if (abs(number - num[right]) < result) {
			one = -number;
			two = num[right];
			result = abs(number - num[right]);
		}
		else if (abs(number - num[left]) < result) {
			one = -number;
			two = num[left];
			result = abs(number - num[left]);
		}
	}
}

int main() {
	int N, number;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> number;
		num[i] = number;
	}
	sort(num, num + N);
	for (int i = 0; i < N; i++) {
		if (num[i] < 0) binary_search(-num[i], N);
		else if (num[i] == 0) {
			if (abs(num[i - 1]) < result) {
				one = num[i - 1];
				two = 0;
			}
			else if (abs(num[i + 1]) < result) {
				one = 0;
				two = num[i + 1];
			}
		}
		if (flag == 1) break;
	}
	cout << one << " " << two;
}