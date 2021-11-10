//11399. ATM
#include <iostream>
using namespace std;

int main() {

	int N;
	int P[1001];
	int sum = 0;

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	cin >> N;
	for (int i = 1; i <= N; i++) {
		cin >> P[i];
	}
	int temp;
	for (int i = 1; i <= N; i++) {
		for (int j = 1; j < N; j++) {
			if (P[j] > P[j + 1]) {
				temp = P[j];
				P[j] = P[j + 1];
				P[j + 1] = temp;
			}
		}
	}
	//정렬 잘 됐는지 확인
//	for (int i = 1; i <= N; i++) {
//		cout << P[i] << " ";
//	} 
//	cout << "\n";

	int n = N;
	for (int i = 1; i <= N; i++) {

		sum += P[i] * n;
		n--;
	}
	cout << sum << endl;
	return 0;
}