//2491. 수열
#include <iostream>
#include <algorithm>
#define MAX 100010
using namespace std;

int arr[MAX];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	int answer = 1;
	int len = 1;
	int N;

	cin >> N;
	//입력받기
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	len = 1;
	//숫자들이 커진다
	for (int i = 1; i < N; i++) {
		if (arr[i] <= arr[i - 1]) {
			len++;
		}
		else len = 1; //끊기면 1로 초기화
		answer = max(answer, len);
	}
	len = 1;
	//숫자들이 작아진다
	for (int i = 1; i < N; i++) {
		if (arr[i] >= arr[i - 1]) {
			len++;
		}
		else len = 1; //끊기면 1로 초기화
		answer = max(answer, len);
	}

	cout << answer ;
	return 0;
}
//범위를 잘못설정했는지 9번이나 틀렸다.