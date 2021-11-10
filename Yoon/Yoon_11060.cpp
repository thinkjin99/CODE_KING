//11060. 점프 점프
#include <iostream>
using namespace std;
int A[1001];
int DP[1001];

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> A[i];
		DP[i] = 987654321;
	}
	DP[0] = 0;
	
	for (int i = 0; i < N; i++) {
		for (int j = 1; j <= A[i]; ++j) { //점프할 수 있는 값
			if (i + j >= N) { //끝까지 갔을 경우 break
				break;
			}
			if (DP[i + j] > DP[i] + 1) { //i에서 j만큼 점프해서 한번도 안갔으면
				DP[i + j] = DP[i] + 1; //점프해서 i까지 갔던 수 + 1
			}
		}
	}
	if (DP[N - 1] == 987654321) { //N-1까지 못갔으면 -1 return
		DP[N - 1] = -1;
	}
	cout << DP[N - 1];
	return 0;
}