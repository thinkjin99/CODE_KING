//파일 합치기3
//허프만 문제 같음.
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


int main() {

	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0); 

	int T; //테스트 데이터 개수
	int K; //소설을 구성하는 장의 수
	int k; //각각의 장까지 수록한 파일 크기
	long long ans = 0;


	cin >> T;
	
	//for (int i = 0; i < T; i++) {
	while(T--){
		cin >> K;
		priority_queue<long long, vector<long long>, greater<long long>> pq;

		//for (int j = 0; j < K; j++) {
		while(K--){
			cin >> k;
			pq.push(k);	//우선순위 큐에 넣음
			//왜냐하면 작은 것들먼저 더하고 그다음 작은것과 더하기 위해서는
			//우선순위 큐에 넣어서 더한 숫자들은 빼고 더한 결과를 다시 넣는다.
		}
		
		ans = 0;

		while (!pq.empty()) {
			if (pq.size() == 1) break;

			long long first = pq.top();
			pq.pop(); //제일 작은 숫자
			long long second = pq.top();
			pq.pop(); //그다음 작은 숫자

			ans += first + second; 
			pq.push(first + second); //둘이 더해서 우선순위 큐에 넣음
		}
		pq.pop();
		cout << ans << "\n";
	}
	return 0;
}