#include <iostream>
#include <map>
#include <algorithm>
using namespace std;

//해당 숫자를 제외한 다른 숫자의 합으로 해당 숫자를 표현할 수 있는 숫자

int main() {

	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	int N;
	int cnt=0;
	int A[2001] = { 0, };

	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
	}

	sort(A, A + N);

	for (int i = 0; i < N; i++) {
		int ans = A[i];
		int L = 0;
		int R = N - 1;
		
		//투포인터 알고리즘 활용
		while (L < R) {
			if (A[L] + A[R] == ans) {
				if (L != i && R != i) { //L과 R이 다름을 check
					cnt++;
					break;
				}
				else if (L == i) {
					L++;
				}
				else if (R == i) {
					R--;
				}
			}
			else if (A[L] + A[R] < ans) {
				L++; 
			}
			else {
				R--;
			}
			
		}
	}
	cout << cnt;
	return 0;
}

//소감: 트리할 때 보다 문제를 이해하는게 쉬웠지만 알고리즘을 짜는데 어려움이 있었다.
// 투포인터 알고리즘  https://butter-shower.tistory.com/226
//참고 https://coding-insider.tistory.com/entry/%EB%B0%B1%EC%A4%80-1253-%EC%A2%8B%EB%8B%A4-CC
