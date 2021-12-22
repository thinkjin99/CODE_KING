//2193. 이친수
#include <iostream>
using namespace std;

long long DP[100][2]; //DP[자릿수][마지막 숫자] 
long long result;
//왜 int가 아니라 longlong 일까 -> DP크기를 고려해서 longlong 타입으로 선언해줘야한다
// 계속 틀렸다길래 찾아보니까 그렇다네...

int main() {
	int N;
	cin >> N;

	DP[1][0] = 0; //한자리인데 0으로 끝나는 이친수 없음
	DP[1][1] = 1; //한자리인데 1로 끝나는 이친수 1개

	for (int i = 2; i <= N; i++) {
		DP[i][0] = DP[i - 1][0] + DP[i - 1][1]; //0으로 끝나면 앞에 0이든 1이든 상관x
		DP[i][1] = DP[i - 1][0]; //1로 끝나며 앞에 0으로 끝나야함
	}
	result = DP[N][0] + DP[N][1]; //0으로 끝나는 이친수 개수 + 1로 끝나는 이친수 개수
	
	cout << result << endl;
	return 0;
}