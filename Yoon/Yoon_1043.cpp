//1043. 거짓말
#include <iostream>
using namespace std;

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	int N, M;//N=사람수, M=파티수
	int num;// 사람의 수
	int Tn;//진실을 아는 사람의 번호
	int t[51] = { 0 };//진실을 아는 사람의 번호에 1을 표시
	int mn[51][51] = { 0 };//[각 파티마다 오는 사람의수][번호]
	int arr_index[50] = { 0 };
	int val[50] = { 0 }; //거짓말의 여부
	int result = 0;
	
	cin >> N >> M;
	cin >> num; //진실을 아는 사람의 수
	for (int i = 0; i < num; i++) {
		cin >> Tn;
		t[Tn] = 1;
	}
	for (int i = 0; i < M; i++) {
		cin >> num; //파티마다 오는 사람의 수
		arr_index[i] = num; //파티마다 오는 사람의 수 배열에 저장
		for (int j = 0; j < num; j++) {
			cin >> mn[i][j];
		}
	}
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < arr_index[i]; j++) {
			int v = mn[i][j];
			if (t[v] == 1) {//진실을 알고 있다면
				val[i] = 1; //거짓말을 할 수 없다.

				bool ans = true;
				for (int k = 0; k < arr_index[i]; k++) {
					if (t[mn[i][k]] == 0 && j != k) { 
						//i번째 파티에 j가 진실을 알고있는데 k가 모르고 j랑 k의 번호가 다르면
						//k도 진실을 알고 있다는 뜻으로
						ans = false;
						t[mn[i][k]] = 1; //k번의 사람도 진실을 알고 있음을 표시
					}
				}
				if (ans == false) { //처음 파티부터 확인
					i = -1;
					break;
				}
			}
		}
	}
	for (int i = 0; i < M; i++) {
		if (val[i] == 0) { //거짓말을 할 수 있다면
			result++;
		}
	}
	cout << result << endl;
	return 0;

}