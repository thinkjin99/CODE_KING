//2225. 합분해
#include <iostream>
#define MAX 201
#define mod 1000000000
using namespace std;

int main() {

	//ios_base::sync_with_stdio(0);
	//cin.tie(0); cout.tie(0);

	int N, K;
	long long arr[MAX][MAX] = { 0 };
	//
	cin >> N >> K;

	for (int i = 0; i <= K; i++) {
		arr[1][i] = i; //N이 1일때 합이 될수 있는 방법은 K수
	}
	for (int n = 2; n <= N; n++) { //두개 이상 더할때
		for(int k = 1; k <= K; k++){
			arr[n][k] = (arr[n-1][k]+arr[n][k-1]) % mod;
		}
	}
	
	cout << arr[N][K] << endl;

	return 0;

}