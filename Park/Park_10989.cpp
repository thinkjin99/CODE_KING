#include <iostream>
#include <algorithm>
using namespace std;

int main() {

	int N;
	cin >> N;

	// 시간 초과 해결할 땐 이만한 게 없지~
	ios_base::sync_with_stdio(0);
	cin.tie(0);

	// 입력받을 수 있는 수 크기의 배열 생성
	int arr[10001] = { 0, };

	int max = 0;

	// 입력 받을 때마다 그 배열 해당 위치에 ++ 수행
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		arr[temp]++;
		if (max < temp)
			max = temp;
	}

	// 배열의 i번째에 값이 몇 개 있는지는 arr[i] 통해서 찾아낼 수 있음. 거기에 들어있는 값만큼 출력해주기!
	for (int i = 1; i <= max; i++) {
		while (arr[i]) {
			cout << i << "\n";
			arr[i]--;
		}
	}

	return 0;
}
